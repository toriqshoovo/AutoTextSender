import pyautogui
import time
import random
for i in range(0,100):
    r = random.randint(0, 5)
    n = random.randint(1,3)
    dott = "." * r
    time.sleep(2)
    pyautogui.typewrite(f"Write me here{dott}")
    time.sleep(2)
    pyautogui.press("enter")
    if i%n == 1:
        r = random.randint(1, 4)
        dott = "." * r
        pyautogui.typewrite(f"I am here{dott}")
        time.sleep(2)
        pyautogui.press("enter")
