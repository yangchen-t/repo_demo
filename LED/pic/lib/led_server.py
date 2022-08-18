#!/usr/bin/env python3 

import ctypes

import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, HistoryPolicy, ReliabilityPolicy
from std_msgs.msg import UInt8

from flask import Flask, request, jsonify
from flask import make_response, json
import gzip

import os 
from threading import Lock
import threading
import signal
from time import sleep
import datetime
import requests



POST_SERVER_TIMEOUT = 3.0
QOMOLO_ROBOT_ID = os.environ.get('QOMOLO_ROBOT_ID')
if QOMOLO_ROBOT_ID is None:
    print("Missing environment variable: 'QOMOLO_ROBOT_ID'")
    exit()

class LedServer(Node):
    def __init__(self):
        super().__init__('LED_node')
        self.mutex = Lock() 

        self.qos_setting = 1
        latching_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
        )

        #sub
        self.LED_SUB = self.create_subscription(
        UInt8, QOMOLO_ROBOT_ID + '/agent/led_display', self.led_number, 10
        )
        print("ok")
    
    def led_number(self,msg):
        data = msg.data
        print("received image_number: %s" % data)
        with open("/scripts/pic/lib/numbers.csv","w+") as f:
            f.write(str(data))
            return data


def ros2_thread(node):
    print('entering ros2 thread')
    # rclpy.spin(node)
    while rclpy.ok():
        rclpy.spin_once(node)
        sleep(0.01)
    print('leaving ros2 thread')


def sigint_handler(signal, frame):
    """
    SIGINT handler
    We have to know when to tell rclpy to shut down, because
    it's in a child thread which would stall the main thread
    shutdown sequence. So we use this handler to call
    rclpy.shutdown() and then call the previously-installed
    SIGINT handler for Flask
    """
    rclpy.shutdown()
    if prev_sigint_handler is not None:
        prev_sigint_handler(signal)

rclpy.init(args=None)
ros2_node = LedServer()

threading.Thread(target=ros2_thread, args=[ros2_node]).start()
prev_sigint_handler = signal.signal(signal.SIGINT, sigint_handler)

"""
ll = ctypes.cdll.LoadLibrary

lib = ll("./libbx_sdkDual.so")

# pIP 控制器IP
# nPort 控制器端口
# color LED屏颜色类型，详见 E_ScreenColor_G56 声明
# uAreaId 区域的ID号
# uAreaX 区域left坐标
# uAreaY 区域top坐标
# uWidth 区域宽度
# uHeight 区域高度
# pheader 显示属性EQpageHeader_G6
# picPath 显示图片路径
pIP = "192.168.112.11"
nPort = 5005
color = 2
uAreaId = 0
uAreaX = 0
uAreaY = 0
uWidth = 64
uHeight = 32
pheader1 = [ #[0x04,0x01,10,500,1,128,0x00,0x00,1,12,0xff00ff,0,0,0,0,0,0]

        "DisplayMode": "0x04",
        "ClearMode" : 0x01,
        "Speed" : 10,
        "stayTime" : 500000,
        "RepeatTime" : 1,
        "ValidLen" : 128,
        "CartoonFrameRate" : 0x00,
        "BackNotValidFlag" : 0x00,
        "arrMode" : "eMULTILINE", #eSINGLELINE;
        "fontSize" : 12,
        "color" : 0xff00ff,  #eGREEN
        "fontBold" : false,
        "fontItalic" : false,
        "tdirection" : pNORMAL,
        "txtSpace" : 0,
        "Valign" : 2,
        "Halign" : 3
]
with open("numbers.csv","r") as f:
        data = f.read()
        picPath = "./pic/" + str(data) + ".png"

lib.bxDual_dynamicArea_AddAreaPic_6G(pIP, 5005, color, uAreaId, uAreaX, uAreaY, uWidth, uHeight, pheader1, picPath)
print("ok")
#print(request_send_pic)
"""
