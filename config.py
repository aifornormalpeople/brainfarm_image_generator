
"""
Application configuration and constants.
Loads environment variables from a .env file.
"""

import os
from dotenv import load_dotenv

# Load .env (must contain OPENAI_API_KEY)
load_dotenv()

# --- API Key ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# --- OpenAI Model Settings ---
MODEL_ID = "gpt-image-1"
SIZES_GPT1 = ["auto", "1024x1024", "1536x1024", "1024x1536"]
QUALITIES_GPT1 = ["auto", "high", "medium", "low"]
BACKGROUNDS_GPT1 = ["auto", "transparent", "opaque"]
OUTPUT_FORMATS_GPT1 = ["png", "jpeg", "webp"]
MODERATION_LEVELS_GPT1 = ["auto", "low"]
MAX_CHARS_GPT1 = 32000

# --- File & Directory Settings ---
GENERATED_IMAGES_DIR = "generated_images"  # Where generated images are saved
GALLERY_THUMBNAIL_SIZE = (100, 100)            # Thumbnail size in the gallery
SYSTEM_PROMPTS_FILE = "system_prompts.json"  # File to persist custom prompts
DEFAULT_SYSTEM_PROMPT_NAME = "None"            # “No prompt” option label

# --- Theme Definitions ---
DARK_THEME = {
    "BG_COLOR": "#2E2E2E",
    "FG_COLOR": "#FFFFFF",
    "FRAME_BG_COLOR": "#3C3C3C",
    "BUTTON_BG_COLOR": "#555555",
    "BUTTON_FG_COLOR": "#FFFFFF",
    "DISABLED_FG_COLOR": "#999999",
    "CANVAS_BG": "#4A4A4A",
    "TEXT_BG": "#4F4F4F",
    "TEXT_FG": "#FFFFFF",
    "ENTRY_BG": "#4F4F4F",
    "ENTRY_FG": "#FFFFFF",
    "LISTBOX_BG": "#4F4F4F",
    "LISTBOX_FG": "#FFFFFF",
    "SELECT_BG": "#606060",
    "STATUS_FG_ERROR": "red"
}

LIGHT_THEME = {
    "BG_COLOR": "#F0F0F0",
    "FG_COLOR": "#000000",
    "FRAME_BG_COLOR": "#E0E0E0",
    "BUTTON_BG_COLOR": "#D0D0D0",
    "BUTTON_FG_COLOR": "#000000",
    "DISABLED_FG_COLOR": "#A0A0A0",
    "CANVAS_BG": "#FFFFFF",
    "TEXT_BG": "#FFFFFF",
    "TEXT_FG": "#000000",
    "ENTRY_BG": "#FFFFFF",
    "ENTRY_FG": "#000000",
    "LISTBOX_BG": "#FFFFFF",
    "LISTBOX_FG": "#000000",
    "SELECT_BG": "#0078D7",
    "STATUS_FG_ERROR": "#CC0000"
}