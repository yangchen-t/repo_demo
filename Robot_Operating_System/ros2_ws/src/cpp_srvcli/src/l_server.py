#!/usr/bin/env python3 

import rclpy
from rclpy.node import Node
from message_interfaces.srv import Test


flag = False

class MinimalService(Node):
    def __init__(self):
        super().__init__('minimal_service')
        self.srv = self.create_service(Test, 'dadeng_test_server', self.add_two_ints_callback)

    def add_two_ints_callback(self, request,response):
        global flag
        flag = bool(1-flag)
        # response = response.result
        if flag :
            self.get_logger().info("this is %s" % request.ALL_COMPENSATE_LAMP_OFF)
            print("The headlights are about to turn on")
        # print(response)
        else:
            self.get_logger().info("this is %s" % request.FRONT_COMPENSATE_LAMP_ON)
            print("The headlights are about to turn off")
            
        return response

def main(args=None): 
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
