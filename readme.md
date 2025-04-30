# OpenAI Image Generator

A friendly, customizable desktop app for generating and editing images with OpenAI’s Image APIs.
Built with Python and Tkinter—no web server required.

---

## Table of Contents

- [🚀 Features](#-features)
- [🛠️ Prerequisites](#️-prerequisites)
- [📦 Installation](#-installation)
- [🎬 Quick Start Guide](#-quick-start-guide)
  - [Generate an Image](#generate-an-image)
  - [Edit an Existing Image (Reference Mode)](#edit-an-existing-image-reference-mode)
  - [Inpainting (Mask-based Edits)](#inpainting-mask-based-edits)
  - [Save & Browse Generated Images](#save--browse-generated-images)
  - [Manage System Prompts](#manage-system-prompts)
- [🗂️ Project Structure](#️-project-structure)
- [💡 Tips & Tricks](#-tips--tricks)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 🚀 Features

-   **Generate images**: Create images from text prompts with options for size, quality, style, and more.
-   **Reference-mode edits**: Tweak an existing image by providing it as a reference alongside a new prompt.
-   **Inpainting**: Load an image, draw a transparent mask over areas to change, and supply a prompt to fill the masked area.
-   **System Prompts**: Create, save, and reuse custom "system" prompts to guide or reframe your image generations consistently.
-   **Gallery Browser**: View a thumbnail grid of all generated images, navigate through them, and easily download individual images.
-   **Dark & Light Themes**: Toggle the UI theme on the fly.
-   **Offline UI**: Runs entirely as a local desktop application without needing a web server or internet connection (except for API calls).

---

## 🛠️ Prerequisites

-   Python 3.8+ installed.
-   An [OpenAI API key](https://platform.openai.com/account/api-keys).
-   Access to a terminal or command prompt.

---

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/openai-image-generator.git](https://github.com/yourusername/openai-image-generator.git)
    cd openai-image-generator
    ```
    *(Replace `yourusername` with the actual username/organization)*

2.  **Create and activate a virtual environment** (optional but highly recommended):
    ```bash
    # Create the environment
    python3 -m venv .venv

    # Activate the environment
    # On macOS / Linux:
    source .venv/bin/activate
    # On Windows PowerShell:
    .\.venv\Scripts\Activate.ps1
    # On Windows Command Prompt:
    .\.venv\Scripts\activate.bat
    ```

3.  **Install dependencies:**
    ```bash
    pip install --upgrade pip
    pip install -r requirements.txt
    ```

4.  **Set up your API key:**
    Create a file named `.env` in the project's root directory and add your API key:
    ```plaintext
    # .env
    OPENAI_API_KEY=sk-YourSecretApiKeyGoesHere
    ```
    *(Replace `sk-YourSecretApiKeyGoesHere` with your actual OpenAI API key)*

5.  **Run the application:**
    ```bash
    python main.py
    ```

---

## 🎬 Quick Start Guide

### Generate an Image

1.  Navigate to the **Generate / Reference** tab.
2.  (Optional) Select a pre-saved **System Prompt** from the dropdown.
3.  Enter your desired image description in the **User Prompt** text box.
4.  Configure options like **Number of Images**, **Size**, **Quality**, **Style**, etc.
5.  Click the **Generate Image** button.

### Edit an Existing Image (Reference Mode)

1.  Go to the **Generate / Reference** tab.
2.  Click **Select Reference Image** and choose a local PNG, JPG, or WEBP file.
3.  *(Note: The 'Options (No Reference)' section will be disabled while a reference image is loaded).*
4.  Enter a new **User Prompt** describing the desired changes or the new image based on the reference.
5.  Click the **Generate Image** button.

### Inpainting (Mask-based Edits)

1.  Switch to the **Inpaint / Edit** tab.
2.  Click **Load Image for Inpainting** and select a local PNG file.
3.  Using the red brush that appears on the image canvas, draw over the areas you want OpenAI to replace or modify. **Important:** Only the red-masked areas will be sent for modification.
4.  Enter a **User Prompt** describing what should appear in the masked areas.
5.  Set the desired **Number of Images**, **Size**, and **Quality**.
6.  Click the **Inpaint Image** button.

### Save & Browse Generated Images

1.  After a successful generation or edit, the first resulting image appears in the **Output Image** pane.
2.  Click **Download This Image** to save the currently displayed image to a location of your choice.
3.  Switch to the **Gallery** tab to see thumbnails of all images generated during the current session.
4.  Click any thumbnail to view it larger in the main display area or use the **Previous**/**Next** buttons.

### Manage System Prompts

1.  Go to the **System Prompts** tab.
2.  To add a new prompt:
    * Click **New Prompt**.
    * Enter a unique **Prompt Name** (for the dropdown menus).
    * Enter the guiding text in the **Prompt Body**.
    * Click **Save Prompt**.
3.  To edit or delete:
    * Select an existing prompt from the list on the left.
    * Modify the Name or Body and click **Save Prompt** to update.
    * Click **Delete Selected** to remove it.
4.  Saved prompts automatically appear in the **System Prompt** dropdowns on the **Generate / Reference** and **Inpaint / Edit** tabs.

---

## 🗂️ Project Structure

```text
.
├── .env                  # Stores your OPENAI_API_KEY (create this manually)
├── .gitignore            # Specifies intentionally untracked files (e.g., .env, __pycache__)
├── main.py               # Main application entry point script
├── config.py             # Contains constants, default settings, and theme definitions
├── api_handler.py        # Handles interaction with the OpenAI API
├── ui_handler.py         # Manages the Tkinter GUI, event handling, and application state
├── requirements.txt      # Lists Python package dependencies
├── system_prompts.json   # Stores saved system prompts (auto-created/managed by the app)
└── generated_images/     # Default directory for saved image outputs (auto-created)


```
💡 Tips & Tricks
The combined length of the System Prompt and User Prompt is limited by the API (currently around 4000 characters for DALL-E 3, check OpenAI docs for specifics). The app may truncate or warn if exceeded.
For inpainting, ensure your mask is drawn directly on the preview canvas within the app. The red color indicates the masked area.
Generating multiple images or high-resolution images can take some time depending on the OpenAI API load and your connection. Check the status bar for progress updates.
You can customize default UI colors, sizes, or generation parameters by editing the config.py file.
Error messages from the API or application are typically displayed in the status bar at the bottom or via pop-up dialogs for critical issues.
🤝 Contributing
Contributions are welcome! Please follow these steps:

Fork the repository on GitHub.
Create a new feature branch:
Bash
```
git checkout -b feature/your-amazing-feature
```
Commit your changes:
Bash
```
git commit -am 'Add some amazing feature'
```
Push the branch to your fork:
Bash
```
git push origin feature/your-amazing-feature
```
Open a Pull Request back to the original repository.

📄 License
This project is released under the MIT License. See the LICENSE file (if included) or the standard MIT License text for details. Feel free to use, adapt, and extend!

Enjoy generating awesome images with a sprinkle of AI magic! ✨