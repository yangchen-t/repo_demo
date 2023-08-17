#!/usr/bin/env python3

import os,time,datetime,pytz

import rclpy
from rclpy.node import Node
from planning_ros_msgs.msg import Trajectory



class Subscriber(Node):
    def __init__(self,name):
        super().__init__(name)
        self.subscriber = self.create_subscription(Trajectory,
                                                  '/tj003/test_plan/problem',
                                                  self.sub_callback,
                                                   10)

    def sub_callback(self,msg):
        print(time.time())
        print(msg)
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber("test_sub_localization")
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()


