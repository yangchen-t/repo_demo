import math
import time
import csv
import os
import rclpy
from rclpy.node import Node
from rclpy.time import Duration
from qomolo_control_msgs.msg import CmdFourWheelSteering
from qomolo_control_msgs.msg import ChassisStateFeedback

env = os.getenv("QOMOLO_ROBOT_ID")

class NavigationCmdPublisher(Node):
    
    def __init__(self):
        super().__init__('cmd_publisher')
        self.cmd_publisher = self.create_publisher(CmdFourWheelSteering, '/' + str(env) + '/navigation/cmd_4ws', 10)
        self.chassis_state_feedback_sub_ = self.create_subscription(ChassisStateFeedback, 
                                                '/' + str(env) + '/chassis_state_feedback', self.chassis_state_callback, 10)
        timer_period = 0.02 #50hz
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.start_time = self.get_clock().now()
        self.start_time = time.time()
        # print("start time: ", self.start_time)
        self.current_time = self.get_clock().now()
        self.duration = 0.0
        # target_angle shoule be less than max value because of inevitable overshoot
        self.target_angle = 0.3
        self.max_angle = 0.3
        self.delay = 0.0
        self.overshoot = 0.0
        self.overshoot_last = 0.0
        self.chassis_speed = 0.0
        self.front_wheel_angle = 0.0
        self.rear_wheel_angle = 0.0
        self.cmd_reached_target_angle_time = 0.0
        self.chassis_reached_target_angle_time = 0.0
        self.cmd_reached_max_angle_time = 0.0
        self.chassis_reached_max_angle_time = 0.0
        self.starting_delay = 0.0

        self.start_steering = True
        self.cmd_reached_target_angle = True
        self.chassis_reached_target_angle = True
        self.cmd_reached_max_angle = True
        self.chassis_reached_max_angle = True

        self.savecsv_path = os.path.join("/debug", env + "_chassis_steer_test_" + str(self.start_time) + ".csv")
        print("csv path:",self.savecsv_path)
        self.f = open(self.savecsv_path, "a", newline="")
        self.csv_writer = csv.writer(self.f, dialect="excel")
        self.row = ["cmd_velocity", "chassis_velocity", "cmd_front_steering", "cmd_rear_steering", "chassis_front_steering", "chassis_rear_steering", "time"]
        self.csv_writer.writerow(self.row)
    
    def timer_callback(self):
        self.current_timestamp = self.get_clock().now()
        self.current_time = time.time()
        self.duration = self.current_time - self.start_time
        # print("duration: ", self.duration)
        cmd = CmdFourWheelSteering()
        cmd.header.stamp = self.current_timestamp.to_msg()
        # velocity enable mode
        cmd.control_mode = 0
        cmd.base_speed = 0.03
        # 2s a period, but for real ws, chassis cannot response so fast
        # cmd.front.steering_angle = self.max_angle * math.sin(self.duration * math.pi)
        # cmd.rear.steering_angle = -cmd.front.steering_angle
        # steering mode / crabbing mode
        cmd.front.steering_angle = 0.3
        cmd.rear.steering_angle = -0.3
        # print("cmd.front.angle: ", cmd.front.steering_angle)
        # print("chassis.front_wheel_angle: ", self.front_wheel_angle)

        row = [cmd.base_speed, self.chassis_speed, cmd.front.steering_angle, cmd.rear.steering_angle, 
                self.front_wheel_angle, self.rear_wheel_angle, self.current_time]
        self.csv_writer.writerow(row)

        # calculate starting delay
        if((math.fabs(self.front_wheel_angle) > 0.005) & (self.start_steering)):
            # print("-----------------------------------------------")
            print("starting delay: ", self.duration)
            self.start_steering = False
            self.starting_delay = self.duration
            print("-----------------------------------------------")

        # calculate reaching target angle delay
        if((math.fabs(cmd.front.steering_angle - self.target_angle) <= 0.01) & (self.cmd_reached_target_angle)):
            self.cmd_reached_target_angle_time = self.duration
            self.cmd_reached_target_angle = False
        if((math.fabs(self.front_wheel_angle - self.target_angle) <= 0.01) & (self.chassis_reached_target_angle)):
            self.chassis_reached_target_angle_time = self.duration
            # self.delay = self.chassis_reached_target_angle_time - self.cmd_reached_target_angle_time
            self.delay = self.chassis_reached_target_angle_time - self.starting_delay
            self.chassis_reached_target_angle = False
            print("cmd_reached_target_angle_time: ", self.cmd_reached_target_angle_time)
            print("chassis_reached_target_angle_time:", self.chassis_reached_target_angle_time)
            print("-----------------------------------------------")
            print("reach target angle: ", self.target_angle) 
            print("delay: ", self.delay)
            print("-----------------------------------------------")

        # calculate overshoot
        if((math.fabs(cmd.front.steering_angle - self.max_angle) <= 0.01) & (self.cmd_reached_max_angle)):
            self.cmd_reached_max_angle_time = self.duration
            self.cmd_reached_max_angle = False
        if((self.delay >= 0.1) & (self.chassis_reached_max_angle)):
            self.chassis_reached_max_angle_time = self.cmd_reached_max_angle_time + self.delay
            # print("duration: ", self.duration)
            # print("self.chassis_reached_max_angle_time: ", self.chassis_reached_max_angle_time)
            # print("minus: ", self.duration - self.chassis_reached_max_angle_time)
            if((self.duration - self.chassis_reached_max_angle_time) >= -0.1):
                self.overshoot = math.fabs(self.front_wheel_angle / self.max_angle)
                if(self.overshoot < self.overshoot_last):
                    print("overshoot: ", self.overshoot_last)
                    self.chassis_reached_max_angle = False
                self.overshoot_last = self.overshoot

        if(self.duration > 2.0):
            cmd.front.steering_angle = 0.0
            cmd.rear.steering_angle = 0.0

        self.cmd_publisher.publish(cmd)
    
    def chassis_state_callback(self, msg):
        chassis_fr = msg.raw_data.front_right_wheel_steering
        chassis_fl = msg.raw_data.front_left_wheel_steering
        chassis_rr = msg.raw_data.rear_right_wheel_steering
        chassis_rl = msg.raw_data.rear_left_wheel_steering
        if (chassis_fr + chassis_fl) < 0.01 :
            self.front_wheel_angle  = (chassis_fl + chassis_fr) / 2.0
        else:
            self.front_wheel_angle = 2.0 * math.atan2(chassis_fl, 1) * math.atan2(chassis_fr, 1) / (math.atan2(chassis_fl, 1) + math.atan2(chassis_fr, 1))
        if (chassis_rr + chassis_rl) < 0.01 :
            self.rear_wheel_angle  = (chassis_rl + chassis_rr) / 2.0
        else:
            self.rear_wheel_angle = 2.0 * math.atan2(chassis_rl, 1) * math.atan2(chassis_rr, 1) / (math.atan2(chassis_rl, 1) + math.atan2(chassis_rr, 1))
        
        self.chassis_speed = (msg.raw_data.front_right_wheel_speed + msg.raw_data.front_left_wheel_speed + msg.raw_data.rear_right_wheel_speed + msg.raw_data.rear_left_wheel_speed) / 4

    def __del__(self):
        self.f.close()
        

def main(args=None):
    rclpy.init(args=args)
    cmd_publisher = NavigationCmdPublisher()
    rclpy.spin(cmd_publisher)

    cmd_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
        

