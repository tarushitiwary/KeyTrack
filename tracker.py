import win32gui

def get_active_window():
    return win32gui.GetWindowText(win32gui.GetForegroundWindow())