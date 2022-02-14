#!/bin/python3
import pyautogui as ui
from time import sleep as sl

ui.FAILSAFE = True

ui.hotkey('alt','tab')
ui.rightClick(x=1081,y=1043)
sl(0.5)

ui.leftClick(x=1048,y=984)
sl(0.5)
ui.leftClick(x=158,y=935)
sl(1)
ui.leftClick(x=1177,y=426)
sl(5)
ui.leftClick(x=590,y=722)
sl(1)
ui.leftClick(x=1628,y=24,internel=0.25)
ui.doubleClick(x=288,y=172)
ui.typewrite('qomolo',internel=0.25)
ui.hotkey('Enter')
ui.typewrite('002')
ui.hotkey('tab')
sl(0.5)
ui.typewrite('qomolo')
ui.leftClick(x=1287,y=665)





