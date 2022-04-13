#!/usr/bin/env python3

import os,time,datetime,pytz

import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

ns = os.getenv("QOMOLO_ROBOT_ID")

class Subscriber(Node):
    def __init__(self,name):
        super().__init__(name)
        self.subscriber = self.create_subscription(Odometry,"/"+ns+
                                                  "/localization/odom",
                                                  self.sub_callback,
                                                   10)

    def sub_callback(self,msg):
        data  = (msg.twist.twist.linear.x)
        with open("test.log",'a') as f:
            f.write(datetime.datetime.now(pytz.timezone('PRC')).strftime("%Y-%m-%d_%H:%M:%S")+",")
            f.write(str(time.time()) + ",")
            f.write("current_linear_x = ")
            f.write(str(data))
            f.write(chr(10))
def main(args=None):
    rclpy.init(args=args)
    node = Subscriber("test_sub_localization")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


