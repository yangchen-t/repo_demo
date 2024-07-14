#!/usr/bin/env python3

import os,time,datetime,pytz

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2

ns = os.getenv("QOMOLO_ROBOT_ID")

class Subscriber(Node):
    def __init__(self,name):
        super().__init__(name)
        self.subscriber = self.create_subscription(PointCloud2,
                                                  "/pcl/output",
                                                  self.sub_callback,
                                                   10)

    def sub_callback(self,msg):
        print(msg)
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber("test_sub_localization")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


