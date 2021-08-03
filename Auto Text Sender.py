import pyautogui
import time
for i in range(0,100):
    time.sleep(2)
    pyautogui.typewrite("Write me here")
    time.sleep(2)
    pyautogui.press("enter")