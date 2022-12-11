#!/bin/python3
import pyautogui
import math


'''for i in range(10):
   pyautogui.moveTo(300, 300, duration=0.25)
   pyautogui.moveTo(400, 300, duration=0.25)
   pyautogui.moveTo(400, 400, duration=0.25)
   pyautogui.moveTo(300, 400, duration=0.25)'''

'''x, y = pyautogui.size()
r = 250 # 圆的半径
# 圆心
o_x = x/2
o_y = y/2
pi = 3.1415926
for i in range(10):  # 转10圈
 for angle in range(0, 360, 5): # 利用圆的参数方程
   xX_1 = o_x + r * math.sin(angle*pi/180)
   yY_2 = o_y + r * math.cos(angle*pi/180)
   pyautogui.moveTo(xX_1,yY_2,duration=0.1)
pyautogui.FAILSAFE = True   #stop'''
