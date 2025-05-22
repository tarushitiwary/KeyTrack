from PIL import ImageGrab
from datetime import datetime
import os

def maybe_capture_screen(key):
    if str(key).lower() in ["'enter'", "Key.enter"]:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        img = ImageGrab.grab()
        os.makedirs("screenshots", exist_ok=True)
        img.save(os.path.join("screenshots", f"{timestamp}.png"))