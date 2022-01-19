#!/bin/python3

import pyautogui as ui
from time import sleep as sl
import logging,time

start_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(start_time)
ui.FAILSAFE = True
##hr1
ui.doubleClick(x=1234,y=277)
ui.doubleClick(x=1683,y=277)
ui.doubleClick(x=1762,y=277)
sl(0.2)
##hr2
ui.doubleClick(x=1234,y=341)
ui.doubleClick(x=1683,y=341)
ui.doubleClick(x=1762,y=341)
sl(0.1)
##hr3
ui.doubleClick(x=1234,y=404)
ui.doubleClick(x=1683,y=404)
ui.doubleClick(x=1762,y=404)
sl(0.1)
##hr4
ui.doubleClick(x=1234,y=472)
ui.doubleClick(x=1683,y=472)
ui.doubleClick(x=1762,y=472)
sl(0.1)
##hr5
ui.doubleClick(x=1234,y=534)
ui.doubleClick(x=1683,y=534)
ui.doubleClick(x=1762,y=534)
sl(0.1)
##hr6
ui.doubleClick(x=1234,y=606)
ui.doubleClick(x=1683,y=606)
ui.doubleClick(x=1762,y=606)
stop_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
print(stop_time)
print('finish')

'''logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='upload.log',
                    filemode='w',##有w和a，w就是写模式，每次都会重新写日志 #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '{ %(created)f- %(funcName)s -  [%(levelname)s] }:= %(message)s'
                    #日志格式
                    )
logging.debug('{0}, {1}, {2}')'''
