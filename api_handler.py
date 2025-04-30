
"""
Handles all OpenAI Image API calls and processes responses/errors.
Each function expects the `app` instance so it can schedule UI updates
via `app.after(...)`.
"""

import io
import os
import base64
import datetime
import traceback
from PIL import Image
from openai import BadRequestError

from config import MODEL_ID, GENERATED_IMAGES_DIR

def call_generate_api(app, prompt, n, **kwargs):
    """
    Calls the OpenAI Image Generation API.
    On success, schedules `process_api_response`.
    On error, schedules `handle_api_error`.
    """
    try:
        response = app.client.images.generate(
            model=MODEL_ID,
            prompt=prompt,
            n=n,
            **kwargs
        )
        app.after(0, process_api_response, app, response, n)
    except BadRequestError as e:
        app.after(0, handle_api_error, app, e, "generating image")
    except Exception as e:
        app.after(0, app.update_status, f"Error generating image: {e}", True)
        traceback.print_exc()

def call_edit_api(app, image_files, prompt, mask_file_obj, n, image_format='PNG', **kwargs):
    """
    Calls the OpenAI Image Edit API.
    Supports both reference (no mask) and inpainting (with mask).
    """
    image_file_obj = None
    try:
        mode = "Inpainting" if mask_file_obj else "Reference"
        image_file_obj = image_files[0]

        # Build `image` parameter
        if mode == "Inpainting":
            image_param = (
                f"image.{image_format.lower()}",
                image_file_obj,
                f"image/{image_format.lower()}"
            )
        else:
            image_param = image_file_obj

        # Assemble parameters
        edit_params = {
            "model": MODEL_ID,
            "image": image_param,
            "prompt": prompt,
            "n": n,
            **kwargs
        }
        if mask_file_obj:
            edit_params["mask"] = ("mask.png", mask_file_obj, "image/png")

        response = app.client.images.edit(**edit_params)
        app.after(0, process_api_response, app, response, n)

    except BadRequestError as e:
        app.after(0, handle_api_error, app, e, mode.lower())
    except Exception as e:
        app.after(0, app.update_status, f"Error {mode.lower()} image: {e}", True)
        traceback.print_exc()
    finally:
        # Always close file handles
        if image_file_obj and not image_file_obj.closed:
            image_file_obj.close()
        if mask_file_obj and not mask_file_obj.closed:
            mask_file_obj.close()

def process_api_response(app, response, num_expected):
    """
    Decodes base64 images, saves each to disk, and displays the first.
    Updates status bar and refreshes gallery afterward.
    """
    if not response or not getattr(response, "data", None):
        app.after(0, app.update_status, "Error: Empty or invalid response data.", True)
        app.after(0, app.clear_output_display)
        return

    saved_count = 0
    first_bytes = None
    first_ext = "png"
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    for i, img_data in enumerate(response.data):
        if hasattr(img_data, "b64_json") and img_data.b64_json:
            try:
                raw = base64.b64decode(img_data.b64_json)
                # detect format
                img = Image.open(io.BytesIO(raw))
                fmt = (img.format or "PNG").lower()
                img.close()
                ext = "jpg" if fmt == "jpeg" else fmt
                fname = f"img_{timestamp}_{i}.{ext}"
                path = os.path.join(GENERATED_IMAGES_DIR, fname)
                with open(path, "wb") as f:
                    f.write(raw)
                saved_count += 1
                if i == 0:
                    first_bytes = raw
                    first_ext = ext
            except Exception as e:
                app.after(0, app.update_status, f"Error processing image {i}: {e}", True)
                traceback.print_exc()
        else:
            print(f"Warning: Image data {i} missing b64_json.")

    # Display first image
    if first_bytes:
        try:
            img = Image.open(io.BytesIO(first_bytes))
            app.generated_image_data = first_bytes
            app.generated_image_format = first_ext
            app.display_output_image(img)
        except Exception as e:
            app.after(0, app.update_status, f"Error displaying first image: {e}", True)
            traceback.print_exc()

    status = f"Processed {saved_count}/{len(response.data)} images. Saved to '{GENERATED_IMAGES_DIR}'."
    app.after(0, app.update_status, status, saved_count != len(response.data))
    app.after(100, app.refresh_gallery)
    app.after(0, app.update_nav_buttons)

def handle_api_error(app, error, action_context):
    """
    Parses and handles OpenAI API errors, showing user-friendly messages.
    """
    msg = f"API Error when {action_context}: "
    detail = ""
    try:
        body = error.response.json()
        detail = body.get("error", {}).get("message", "") or str(error)
    except Exception:
        detail = str(error)

    code = getattr(error, "status_code", None)
    if code == 429:
        msg = "API Error: Rate limit exceeded or quota reached."
    elif code == 401:
        msg = "API Error: Authentication failed. Check your API key."
    elif code == 400 and "Mask image must have transparency" in detail:
        msg = "API Error: Mask issue—ensure your mask has transparency."

    full = f"{msg} {detail}"
    traceback.print_exc()
    app.update_status(full, True)