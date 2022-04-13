import rclpy
from rclpy.node import Node
import numpy as np
from function_control_msgs.msg import FunctionState

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('move_please')
        self.publisher_ = self.create_publisher(FunctionState, '/tj003/function_control/state', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = FunctionState()
        msg.header.frame_id = "map"
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.chassis_ready_sts = True
        msg.parking = False
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
