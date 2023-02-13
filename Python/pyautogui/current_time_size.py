#/bin/python3
import pyautogui
import time 

try:
    while True:
        x,y = pyautogui.position()
        time.sleep(1)
        print(x, y)
except KeyboardInterrupt:
    print('\nExit.')



# while True:
#     x,y=ui.position()
#     print(x, y)