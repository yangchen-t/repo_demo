#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
from planning_ros_msgs.msg import Trajectory, TrajectoryPoint

import time
import random

class MinimalPublisher(Node):
    def __init__(self,name):
        super().__init__(name)
        self.publisher_ = self.create_publisher(Trajectory, '/tj003/test_plan/problem', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Trajectory()
        # msg.header = ""
        point = TrajectoryPoint()
        for i in range(1, 100):
            point.x = random.random()
            point.v = 0.5
            msg.points.append(point)
        msg.dead_distance = 123.2
        msg.stop_index = random.randint(1,100)

        self.publisher_.publish(msg)
        print(msg.stop_index, time.time())

def main(args=None):
    rclpy.init(args=args)
    node = MinimalPublisher("test_sub_localization")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()


        # msg.points.y = 1232.123
        # msg.points.heading_angle = 12
        # msg.points.s = 1
        # msg.points.v = 12
        # msg.points.a = 1
        # msg.points.course_angle = 1
        # msg.points.k = 1
        # msg.points.yaw_rate = 1
        # msg.points.tail_angles = [1,2,3.23,23.1]


        # msg.header.stamp = self.get_clock().now().to_msg()
        # msg.chassis_ready_sts = True
        # msg.parking = False
        # self.publisher_.publish(msg)