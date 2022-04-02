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


class Windows:
    def __init__(self, obs_client):
        self.obs_client = obs_client

    def get_current_process_name(self):
        hwnd = win32gui.GetForegroundWindow()
        _, pid = win32process.GetWindowThreadProcessId(hwnd)

        process = psutil.Process(pid)
        process_name = process.name()

        return process_name

    def __beep(self):
        Beep(200, 2000)

    def __print_window_text(self, obs_client, current_window):
        if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Task Manager":
            obs_client.change_to_starting_soon()
            print("task")

        print(win32gui.GetForegroundWindow())
        print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
        if current_window != win32gui.GetForegroundWindow():
            print(current_window)
        current_window = win32gui.GetForegroundWindow()

    def __window_shenanigangs(self, window):
        win32gui.MoveWindow(window, 0, 0, 500, 500, True)
        pos = GetCursorPos()
        SetCursorPos((pos[0] + 100, pos[1] + 100))


if __name__ == "__main__":
    obs_client = OBS()
    current_window = win32gui.GetForegroundWindow()
    windows_command = Windows(obs_client)
    MessageBox(0, "Listo.", "Ejemplo Windows API", MB_OK)
    while True:
        try:
            process_name = windows_command.get_current_process_name()
            print(process_name)
            time.sleep(0.5)
        except KeyboardInterrupt:
            break
