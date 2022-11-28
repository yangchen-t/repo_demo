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

