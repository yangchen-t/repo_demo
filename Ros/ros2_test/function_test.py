#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
import numpy as np
from planning_ros_msgs.msg import Trajectory

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('move_please')
        self.publisher_ = self.create_publisher(Trajectory, '/tj003/test_plan/problem', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Trajectory()
        # msg.header = ""
        msg.dead_distance = ""
        msg.stop_index = 2
        # msg.points.x = 123.12
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

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
