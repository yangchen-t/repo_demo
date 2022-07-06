
import rclpy
from rclpy.node import Node
from rclpy.time import Duration
import time
import csv
from qomolo_control_msgs.msg import CmdFourWheelSteering
from qomolo_control_msgs.msg import ChassisStateFeedback

import os

env = os.getenv("QOMOLO_ROBOT_ID")

class ControlCmdPublisher(Node):
    
    def __init__(self):
        super().__init__('cmd_publisher')
        self.cmd_publisher = self.create_publisher(CmdFourWheelSteering, '/' + str(env) + '/navigation/cmd_4ws', 10)
        self.chassis_state_feedback_sub_ = self.create_subscription(ChassisStateFeedback, 
                                                '/' + str(env) + '/chassis_state_feedback', self.chassis_state_callback, 10)
        timer_period = 0.02 #50hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.start_time = self.get_clock().now()
        self.current_time = self.get_clock().now()
        self.time = time.time()
        self.duration = 0.0
        #The running target time:
        self.target_speed = 1.0
        self.constant_speed_hold_time = 5.0
        self.speed_hold_time = self.target_speed/0.3 + self.constant_speed_hold_time; 
        #Current speed:
        self.current_speed = 0.0
        self.reached_target_speed_first = False
        #In time-mode: give the cmd speed for a constant time and then give 0 speed;
        #In non-time-mode: give target speed cmd until current reaches it, and holds the speed for seconds then give 0 speed;
        self.time_mode = False
        self.target_speed_first_reach_time = self.get_clock().now()

        self.csv_time = time.time()
        self.savecsv_path = os.path.join("/debug", env + "_chassis_speed_test_" + str(self.csv_time) + ".csv")
        print("csv path:",self.savecsv_path)
        self.f = open(self.savecsv_path, "a", newline="")
        self.csv_writer = csv.writer(self.f, dialect="excel")
        self.row = ["cmd_velocity", "chassis_velocity",  "time"]
        self.csv_writer.writerow(self.row)
    
    def timer_callback(self):
        self.current_time = self.get_clock().now()
        self.duration = self.current_time - self.start_time
        self.time = time.time()
        cmd = CmdFourWheelSteering()
        cmd.header.stamp = self.current_time.to_msg()
        cmd.control_mode = 0
        # print("Time: ", self.duration)
        print("current speed: ", self.current_speed)
        #In constant-running-time mode:
        if(self.time_mode):
            if(self.duration > Duration(seconds = self.speed_hold_time)):
                cmd.base_speed = 0.0
                print("Slow down...")
            else:
                cmd.base_speed = self.target_speed
                print("Running>>>")
        else: #In target-speed mode:
            if(self.current_speed >= self.target_speed and (not self.reached_target_speed_first)):
                self.reached_target_speed_first = True
                self.target_speed_first_reach_time = self.get_clock().now()
            if(self.reached_target_speed_first):
                print("target speed rearched")
            hold_time_reached = (self.current_time - self.target_speed_first_reach_time) > Duration(seconds = self.constant_speed_hold_time)
            if(self.reached_target_speed_first and hold_time_reached):
                cmd.base_speed = 0.0
                print("Slow down...")
            else:
                cmd.base_speed = self.target_speed
                print("Running>>>")

        row = [cmd.base_speed, self.current_speed,self.time]
        self.csv_writer.writerow(row)
        self.cmd_publisher.publish(cmd)   
    
    def chassis_state_callback(self, msg):
        self.current_speed  = (msg.raw_data.front_right_wheel_speed + 
                                msg.raw_data.front_left_wheel_speed + 
                                msg.raw_data.rear_right_wheel_speed + 
                                msg.raw_data.rear_left_wheel_speed)/4
        

def main(args=None):
    rclpy.init(args=args)
    cmd_publisher = ControlCmdPublisher()
    rclpy.spin(cmd_publisher)

    cmd_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        

