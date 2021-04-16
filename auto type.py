import pyautogui
import time

time.sleep(3)

with open('hi.txt') as f:
    lines = f.readlines()

for line in lines:
    for c in line:
        time.sleep( 0)
        pyautogui.typewrite(c)
 