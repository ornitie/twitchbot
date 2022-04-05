"""import sys
import os

sys.path.append("../")
os.system('cmd /c "notepad"')
"""

import psutil
import win32process
from win32api import Beep, GetCursorPos, SetCursorPos, MessageBox
from win32con import MB_OK
import win32gui
import time
from obs import OBS

if __name__ == "__main__":
    obs_client = OBS()
    # Beep(200, 2000)
    current_window = win32gui.GetForegroundWindow()
    # win32gui.MoveWindow(current_window, 0, 0, 500, 500, True)
    pos = GetCursorPos()
    SetCursorPos((pos[0] + 100, pos[1] + 100))
    MessageBox(0, "Listo.", "Ejemplo Windows API", MB_OK)
    while True:
        try:
            if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Task Manager":
                obs_client.change_to_starting_soon()
                print("task")

            print(win32gui.GetForegroundWindow())
            print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
            if current_window != win32gui.GetForegroundWindow():
                print(current_window)
            current_window = win32gui.GetForegroundWindow()
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
