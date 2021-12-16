import pyautogui
import time

pyautogui.FAILSAFE=False
pyautogui.PAUSE = 0.1

location=pyautogui.locateOnScreen(image='mix.png')
print(location)
x,y= pyautogui.center(location)
print('center()',x,y)
pyautogui.click(x=x,y=y,clicks=1,button='left')

local_mix = pyautogui.locateOnScreen(image='MIX.png')   
print(local_mix)
mix_x,mix_y=pyautogui.center(local_mix)
print('center()',mix_x,mix_y)
pyautogui.click(x=mix_x,y=mix_y,clicks=1,button='left')
# pyautogui.dragRel(xOffset=0, yOffset = 20)
'''location=pyautogui.locateOnScreen(image='termintal.png')
print(location)
x,y= pyautogui.center(location)
print('center()',x,y)
pyautogui.click(x=x,y=y,clicks=1,button='left')'''
print('finist')
