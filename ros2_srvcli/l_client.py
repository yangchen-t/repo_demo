#!/usr/bin/env python3

from std_msgs.msg import String
import sys
from message_interfaces.srv import Test
import rclpy
from rclpy.node import Node

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        self.cli = self.create_client(Test, 'dadeng_test_server')
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        self.pub_function_ext = self.create_publisher(String,"/tj021/function/ext/request",10)
       

    def send_request(self):
        req = Test.Request()
        self.future = self.cli.call_async(req)

def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClientAsync()
    minimal_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
           print("request finish")
           print("close")
        break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


