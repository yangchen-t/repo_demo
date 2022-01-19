#/bin/python3
import pyautogui

try:
    while True:
        x,y = pyautogui.position()
        print(x, y)
except KeyboardInterrupt:
    print('\nExit.')



# while True:
#     x,y=ui.position()
#     print(x, y)