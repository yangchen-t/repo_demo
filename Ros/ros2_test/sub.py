#!/usr/bin/env python3

import os,time,datetime,pytz

import rclpy
from rclpy.node import Node
from igv_agent_msgs.msg import LedDisplay
from rclpy.qos import QoSProfile, QoSReliabilityPolicy


QOMOLO_ROBOT_ID:str = os.getenv("QOMOLO_ROBOT_ID")

class Subscriber(Node):
    def __init__(self,name):
        super().__init__(name)
        qos = QoSProfile(depth=10)
        qos.reliability = QoSReliabilityPolicy.BEST_EFFORT
        self.subscriber = self.create_subscription(LedDisplay,
                                                  QOMOLO_ROBOT_ID + '/agent/led_display',
                                                  self.sub_callback,
                                                   qos)

    def write_msg_to_csv(self, topic_msg):
        print(topic_msg)

    def sub_callback(self,msg):
        self.write_msg_to_csv(msg)
        
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber("test_sub_localization")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()