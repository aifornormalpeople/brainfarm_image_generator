"""
Entry point for the OpenAI Image Generator application.
Initializes and runs the Tkinter UI.
"""
from ui_handler import ImageGeneratorApp

if __name__ == "__main__":
    app = ImageGeneratorApp()
    app.mainloop()