#!/usr/bin/env python3 

import signal
import threading
import json_message_converter
import message_converter
import json
import os
import sys
import re
import shutil
import subprocess
import paramiko
import requests
import math
import time, datetime
import uuid
import glog
import gzip
from time import sleep
from copy import deepcopy
from queue import Queue, Empty
from math import cos, sin, pi
from threading import Lock


import rclpy
from rclpy.node import Node
from rclpy.qos import QoSProfile, DurabilityPolicy, HistoryPolicy, ReliabilityPolicy

from flask import Flask, request, jsonify
from flask import make_response, json
from flask import abort, make_response, render_template

from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped, Quaternion
from spreader_task_client import MinimalActionClient
from rclpy.parameter import Parameter
from std_msgs.msg import UInt8, String

#Lighting 
from function_control_msgs.srv import SetBcm
# navigation messages
from igv_agent_msgs.msg import Location, Position3D, PathPlanningRoute, NaviPoint, AdvisorySpeeds, Deviation, TimeWindow
# devicetask
from igv_agent_msgs.msg import NaviReq
# sub messages
from igv_agent_msgs.msg import Head


VOC_SERVER_URL = os.environ.get('VOC_SERVER_URL')
if VOC_SERVER_URL is None:
    VOC_SERVER_URL = "http://113.31.113.98:19000"
    print("Using default server URL: ", VOC_SERVER_URL)
else:
    #vOC_SERVER_URL = "http://127.0.0.1:8080"
    print("Using VOC_SERVER_URL: ", VOC_SERVER_URL)

POST_SERVER_TIMEOUT = 3.0
QOMOLO_ROBOT_ID = os.environ.get('QOMOLO_ROBOT_ID')
if QOMOLO_ROBOT_ID is None:
    print("Missing environment variable: 'QOMOLO_ROBOT_ID'")
    exit()
print("QOMOLO_ROBOT_ID : {}".format(QOMOLO_ROBOT_ID))


# 必要的环境参数 nas 外网
# QOMOLO_ROBOT_ID = os.getenv('QOMOLO_ROBOT_ID')
subprocess.getoutput("source /opt/qomolo/utils/qomolo_gcs_scripts/log/env")
# 天津车为hostname
HOST = "192.168.103.77"
PORT = 22
USERNAME = "jian.xu"
PASSWORD = "westwell"

# 内网 地面站服务器信息

# 路径参数
VEHICLE_TYPE = "igv"
ROOT_PATH = "/data/qpilot_log/" + VEHICLE_TYPE + "/"
QLOG_PATH = "/debug/qlog/"
CSV_PATH = "/debug/csv/"
LIDAR_ESTOP_PATH = "/debug/lidar_estop_log/"

# 要抽取的日志文件保存位置
SAVE_LOG_PATH =  "/debug/logpush_tmp/tmp/" + QOMOLO_ROBOT_ID
SAVE_LOG_PATH_NEW = "/debug/logpush_tmp/tmp/" + QOMOLO_ROBOT_ID
# 正在执行的标志位
IS_WORKING_FLAG = False




class RosDataNode(Node):
    def __init__(self):
        super().__init__('voc_node')
        self.mutex = Lock()
        self.error_event_url = VOC_SERVER_URL + "/WellGNS/ErrorHistory"
        self.general_info_url = VOC_SERVER_URL + "/WellGNS/GeneralInfo"

        self.qos_setting = 1
        latching_qos = QoSProfile(
            depth=1,
            durability=DurabilityPolicy.TRANSIENT_LOCAL,
            reliability=ReliabilityPolicy.RELIABLE,
            history=HistoryPolicy.KEEP_LAST,
        )

        #function_client
        self.cli = self.create_client(SetBcm, QOMOLO_ROBOT_ID + 'function_control/set_bcm')


        # pub
        self.publisher_navigation_request = self.create_publisher(
            NaviReq, QOMOLO_ROBOT_ID + "/agent/ext/navi/request", latching_qos
        )
        self.publisher_plan_for_display = self.create_publisher(
            String, "/global_plan_from_path_planning", 10
        )
        self.publisher_path_convert = self.create_publisher(
            String, QOMOLO_ROBOT_ID + "/path_convert", latching_qos)
        

        #sub
        self.recv_path = self.create_subscription(
            String, QOMOLO_ROBOT_ID + '/path_convert', self.on_message_navigation, 10)


        self.navi_req_queue = Queue(maxsize=10)

        self.last_login_response_trans_id = ""
        self.last_logout_response_trans_id = ""
        self.last_power_management_request_trans_id = ""
        self.last_mission_request_trans_id = ""
        self.last_mission_cmd_request_trans_id = ""
        self.last_charger_inform_request_trans_id = ""
        self.last_navigation_request_trans_id = ""
        self.last_stop_request_trans_id = ""
        self.last_resume_request_trans_id = ""
        self.last_arrive_status_response_trans_id = ""
        self.last_in_position_request_trans_id = ""
        self.last_align_result_response_trans_id = ""
        self.last_charger_in_pos_request_trans_id = ""
        self.last_fault_release_request_trans_id = ""
        self.last_fault_report_response_trans_id = ""

        # sub
        self.sub_voc_upstream_general = self.create_subscription(
            String, QOMOLO_ROBOT_ID + '/voc/upstream/general', self.callback_voc_upstream_general, 10)

        self.sub_voc_upstream_error_event = self.create_subscription(
            String, QOMOLO_ROBOT_ID + '/voc/upstream/error_event', self.callback_voc_upstream_error_event, 10)


        # pub
        self.pub_goal_pose = self.create_publisher(PoseStamped, QOMOLO_ROBOT_ID + '/goal_pose', 1)
        self.pub_initial_pose = self.create_publisher(PoseWithCovarianceStamped, QOMOLO_ROBOT_ID + '/initialpose', 1)
        self.pub_func_request = self.create_publisher(UInt8, QOMOLO_ROBOT_ID + '/function_control/ext/request', 1)
        self.pub_task_request = self.create_publisher(UInt8, QOMOLO_ROBOT_ID + '/agent/ext/request', 1)
        self.spreader_action_client = MinimalActionClient(QOMOLO_ROBOT_ID + '/container_operation')


    def callback_voc_upstream_general(self, msg):
        print("callback_voc_upstream_general")
        try:
            print(datetime.datetime.now())
            self.send_post_request(json.loads(msg.data), self.general_info_url, POST_SERVER_TIMEOUT)
        except :
            print("Failed to upload information")

    def callback_voc_upstream_error_event(self, msg):
        print("callback_voc_upstream_error_event")
        self.send_post_request(json.loads(msg.data), self.error_event_url, POST_SERVER_TIMEOUT)

    def quaternion_from_yaw(self, yaw):
        quaternion = Quaternion()
        quaternion.w = cos(yaw / 2.0)
        quaternion.x = 0.0
        quaternion.y = 0.0
        quaternion.z = sin(yaw / 2.0)
        return quaternion

    def send_post_request(self, json_payload, request_url, request_timeout = 0.1):
        print("url: %s, post: %s"%(request_url, json_payload))
        self.mutex.acquire()
        data = None
        try:
            r = requests.post(request_url, timeout=request_timeout, json=json_payload)
            data = r.json()
            print("url: %s, post response: %s"%(request_url, data))
        except Exception as e:
            print(e)
            self.mutex.release()
            return None
        self.mutex.release()
        return data

    def pickup_too_close(self, point_list):
        path_guidance_points_list = []
        for idxnp, np in enumerate(point_list):
            if idxnp > 0:
                lp = deepcopy(path_guidance_points_list[-1])
                distance = math.sqrt(
                            math.pow(lp.pos.x - np.pos.x, 2) + 
                            math.pow(lp.pos.y - np.pos.y, 2)
                        )
                if distance < 0.05:
                    if len(np.type):
                        path_guidance_points_list.pop(-1)
                        path_guidance_points_list.append(np)
                        continue
                    else:
                        continue
            path_guidance_points_list.append(np)
        return path_guidance_points_list

 
    def on_message_navigation(self, msg):
        json_msg = self.on_message_pub_rostopic(msg)
        str_msg = String()
        str_msg.data = json.dumps(json_msg)
        self.publisher_plan_for_display.publish(str_msg)
        if json_msg:
            header = Head()
            header.trans_id = json_msg["header"]["transId"]
            if header.trans_id == self.last_navigation_request_trans_id:
                glog.warn("Duplicated message of Navigation Request. Ignored.")
                return
            self.last_navigation_request_trans_id = header.trans_id

            ref_position = Position3D()
            longitude = float(json_msg["body"]["destination"]["refPosition"]["longitude"])
            latitude = float(json_msg["body"]["destination"]["refPosition"]["latitude"])
            json_elevation = json_msg["body"]["destination"]["refPosition"].get("elevation", 0.0)
            if json_elevation is not None:
                elevation = float(json_elevation)
            else:
                elevation = 0.0

            # if self.is_diff_coord:
            #     remote_pose = Pose2D(x=longitude, y=latitude, theta=0.0)
            #     ref_pose = remote_to_local_pose(remote_pose)
            # else:
            #     remote_pose = Pose2D(x=longitude, y=latitude, theta=elevation)
            #     ref_pose = remote_pose

            ref_position.x = longitude
            ref_position.y = latitude
            ref_position.z = elevation

            destination = Location()
            dest_loc_id = json_msg["body"]["destination"].get("locationId", "")
            if dest_loc_id is not None:
                destination.location_id = str(dest_loc_id)
            else:
                destination.location_id = ""
            dest_loc_type = json_msg["body"]["destination"].get("locationType", "")
            if dest_loc_type is not None:
                destination.location_type = str(dest_loc_type)
            else:
                destination.location_type = ""
            dest_description = json_msg["body"]["destination"].get("description", "")
            if dest_description is not None:
                destination.description = str(dest_description)
            else:
                destination.description = ""
            destination.ref_position = ref_position

            path_guidance = PathPlanningRoute()
            path_guidance.route_id = json_msg["body"]["pathGuidance"]["routeId"]
            try:
                points_list = json_msg["body"]["pathGuidance"]["points"]
            except:
                glog.ERROR("ERROR format of pathGuidance")
            finally:
                pass

            path_guidance_points_list = []
            for point in points_list:
                path_guidance_single_point = NaviPoint()
                path_guidance_single_point.heading = int(point["heading"])

                point_laneid = point.get("laneId", 0)
                if point_laneid is not None:
                    path_guidance_single_point.lane_id = int(point_laneid)
                else:
                    path_guidance_single_point.lane_id = 0
                
                point_direction = point.get("direction", 1)
                if point_direction is not None:
                    int_direction = int(point_direction)
                    if int_direction == 2:
                        path_guidance_single_point.direction = -1
                    else:
                        path_guidance_single_point.direction = 1
                else:
                    path_guidance_single_point.direction = 1

                point_type = point.get("type", "")
                if point_type is not None:
                    str_dict_type = str(point_type)
                    path_guidance_single_point.type = str_dict_type
                else:
                    path_guidance_single_point.type = ""

                pos = Position3D()
                longitude = float(point["pos"]["longitude"])
                latitude = float(point["pos"]["latitude"])
                json_elevation = point["pos"].get("elevation", 0.0)
                if json_elevation is not None:
                    elevation = float(json_elevation)
                else:
                    elevation = 0.0
                pos_theta = math.pi / 2.0 - path_guidance_single_point.heading * 0.0125 / 180.0 * math.pi

                # if self.is_diff_coord:
                #     remote_pose = Pose2D(x=longitude, y=latitude, theta=pos_theta)
                #     ref_pose = remote_to_local_pose(remote_pose)
                # else:
                #     remote_pose = Pose2D(x=longitude, y=latitude, theta=elevation)
                #     ref_pose = remote_pose
                # # glog.info("Pose: {}".format(ref_pose))
                # # glog.info("type: {}".format(point_type))

                pos.x = longitude
                pos.y = latitude
                pos.z = elevation
                path_guidance_single_point.pos = pos

                deviation = Deviation()
                dict_deviation = point.get("deviation", None)
                if dict_deviation is not None:
                    deviation.left = int(dict_deviation.get("left", 0))
                    deviation.right = int(dict_deviation.get("right", 0))
                path_guidance_single_point.deviation = deviation


                speeds = AdvisorySpeeds()
                dict_speeds = point.get("speeds", None)
                if (dict_speeds is not None):
                    speeds.vmax = int(dict_speeds.get("vmax", 0))
                    speeds.vmin = int(dict_speeds.get("vmin", 0))
                path_guidance_single_point.speeds = speeds

                time_window = TimeWindow()
                dict_time_window = point.get("timeWindow", None)
                if (dict_time_window is not None):
                    time_window.start = self.time_format_tranformation(str(dict_time_window.get("start", "")))
                    time_window.end = self.time_format_tranformation(str(dict_time_window.get("end", "")))
                path_guidance_single_point.time_window = time_window

                path_guidance_points_list.append(path_guidance_single_point)

            estimated_time = json_msg["body"].get("estimatedTime", "")
            str_estimated_time = ""
            if estimated_time is not None:
                str_estimated_time = str(estimated_time)

            # Pick up points too close
            check_list = deepcopy(path_guidance_points_list)
            path_guidance_points_list.clear()
            path_guidance_points_list = self.pickup_too_close(check_list)
            path_guidance.points = deepcopy(path_guidance_points_list)

            topic_msg = NaviReq()
            topic_msg.head = header
            topic_msg.navi_id = str(json_msg["body"]["naviId"])
            topic_msg.destination = destination
            topic_msg.estimated_time = str_estimated_time
            topic_msg.path_guidance = path_guidance
            topic_msg.route_update = int(json_msg["body"]["routeUpdate"])
            topic_msg.refer_id = str(json_msg["body"]["referId"])
            topic_msg.is_final_navi = bool(json_msg["body"]["isFinalNavi"])
            topic_msg.is_wellnav_plan = False     
            glog.info("Navigation request published.")
            self.publisher_navigation_request.publish(topic_msg)

    def navi_req_timer(self):
        while True:
            try:
                navi_req_msg = self.navi_req_queue.get(block=False)
                glog.info("Navigation task queue size: {}".format(self.navi_req_queue.qsize()))
                glog.info(
                    "Naviation request msg sent. transId: {}, naviId: {}".format(navi_req_msg.head.trans_id, navi_req_msg.navi_id))
                self.publisher_navigation_request.publish(navi_req_msg)
                self.navi_req_queue.task_done()
                time.sleep(1.0)
            except Empty:
                pass
            time.sleep(0.1)


    def on_message_pub_rostopic(self, msg):
        json_msg = dict()
        empty_msg = dict()
        if not msg:
            glog.error("Message is empty, ignoring message.")
            return empty_msg
        try:
            json_msg = json.loads(msg.data)
            # print("ok")
            device_id = json_msg["header"].get("deviceId", "EMPTY_DEVICE_ID")
            # is_chargerinform = json_msg["body"].get("chargerInform", None)
            # if (device_id != self.mqtt_ns) and (is_chargerinform is None):
            #     glog.warn("Message belongs to {}.".format(device_id))
            #     return empty_msg
            msg_body = json_msg.get("body", None)
            if msg_body is None:
                glog.warn("Message body is empty: {}".format(json_msg))
                json_msg["body"] = dict()
            glog.info(" msg: {}".format( json_msg))
            return json_msg
        except json.decoder.JSONDecodeError:
            glog.error("Message is invalid, ignoring message.")
            return empty_msg
        


    def time_format_tranformation(self, str_timestamp):
        utc_timestamp = 0.0
        if len(str_timestamp):
            timestamp = datetime.datetime.strptime(str_timestamp, self.time_format)
            utc_timestamp = timestamp.utcnow().timestamp()
        return utc_timestamp



def ros2_thread(node):
    print('entering ros2 thread')
    # rclpy.spin(node)
    while rclpy.ok():
        rclpy.spin_once(node)
        sleep(0.01)
    print('leaving ros2 thread')


def sigint_handler(signal, frame):
    """
    SIGINT handler
    We have to know when to tell rclpy to shut down, because
    it's in a child thread which would stall the main thread
    shutdown sequence. So we use this handler to call
    rclpy.shutdown() and then call the previously-installed
    SIGINT handler for Flask
    """
    rclpy.shutdown()
    if prev_sigint_handler is not None:
        prev_sigint_handler(signal)



rclpy.init(args=None)
ros2_node = RosDataNode()

threading.Thread(target=ros2_thread, args=[ros2_node]).start()
prev_sigint_handler = signal.signal(signal.SIGINT,sigint_handler)



#logpush
def save_file(save_path, file_list):
    """
    打包文件
    :param save_path: 保存的路径
    :param file_list: 目标文件路径列表
    :return:
    """
    print("---" * 20)
    print("保存的路径:{} length:{}".format(save_path, len(file_list)))
    # print(file_list[:int(len(file_list) / 4)])
    print("---" * 20)
    print("\n")

    # 不存在则创建
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    # 遍历复制文件
    for file in file_list:
        cmd = 'echo nvidia |sudo -S cp -r ' + file + ' ' + save_path
        print(cmd)
        subprocess.getoutput(cmd)


def pack_Qlog_process(target_timestamp, intervals_timestamp=60 * 60 * 12):
    """
    打包指定模块的log文件
    模块:["agent","canbus","control","function_control","keeper","planning","perception","localization"]
    WARNING INFO ERROR 三种等级日志分别打包
    :return:
    """
    module_list = ["agent", "canbus", "control", "function_control", "keeper", "planning", "perception",
                   "localization"]

    for module_name in module_list:
        print("start package {}".format(module_name))
        Qlog_module_pack(module_name, target_timestamp, intervals_timestamp=60 * 60 * 12)


def Qlog_module_pack(module_name, target_timestamp, intervals_timestamp=60 * 60 * 12):
    """
    打包指定模块的Qlog
    agent_core_node.TJ_IGV_32.root.log.INFO.20220330-023005.1062
    :param module_name: 模块名
    :param target_timestamp: 时间点
    :param intervals_timestamp : 前后间隔时间
    :return:
    """
    module_path = os.path.join("/debug/qlog", module_name)
    # max_timestamp = target_timestamp + intervals_timestamp
    # min_timestamp = target_timestamp - intervals_timestamp
    # 模块目录下所有的文件
    module_file_list = [os.path.join(module_path, i) for i in os.listdir(module_path)]
    # 根据日志等级 生成不同的列表
    info_log_list = []
    warning_log_list = []
    error_log_list = []
    unknown_file_list = []
    for log_file in module_file_list:
        if "WARNING" in log_file:
            warning_log_list.append(log_file)
        elif "INFO" in log_file:
            info_log_list.append(log_file)
        elif "ERROR" in log_file:
            error_log_list.append(log_file)
        else:
            unknown_file_list.append(log_file)
    # 完整的日志文件信息对象结构["文件绝对路径","文件最后修改时间（st_mtime）", "文件大小"]
    warning_log_info_list = [[log_file_path, os.stat(log_file_path).st_mtime, os.stat(log_file_path).st_size] for
                             log_file_path in warning_log_list]
    info_log_info_list = [[log_file_path, os.stat(log_file_path).st_mtime, os.stat(log_file_path).st_size] for
                          log_file_path in info_log_list]
    error_log_info_list = [[log_file_path, os.stat(log_file_path).st_mtime, os.stat(log_file_path).st_size] for
                           log_file_path in error_log_list]
    # 过滤出在时间区间的日志文件 获取日志文件最后修改的系统时间 在三个小时之内的前后两个文件
    all_save_log = []  # 过滤后要保存的文件列表
    for log_info in warning_log_info_list:
        # 时间差值 6小时内都保存
        if abs(log_info[1] - target_timestamp) < 60 * 60 * 12:
            all_save_log.append(log_info[0])
    for log_info in error_log_info_list:
        # 时间差值 6小时内都保存
        if abs(log_info[1] - target_timestamp) < 60 * 60 * 12:
            all_save_log.append(log_info[0])
    for log_info in info_log_info_list:
        # 时间差值 6小时内都保存
        if abs(log_info[1] - target_timestamp) < 60 * 60 * 12:
            all_save_log.append(log_info[0])
    # 将日志文件复制到文件夹中
    save_log_path = os.path.join(SAVE_LOG_PATH, "qlog", module_name)
    # 打包过滤出的日志文件
    save_file(save_log_path, all_save_log)

    print("{} pack ok".format(module_name))


def pack_csv_process(target_timestamp, intervals_timestamp=60 * 60 * 12):
    """
    打包csv文件
    trajectory_conversion时间敏感 半个小时以内的文件
    :param intervals_timestamp: 时间区间
    :return:
    """
    csv_path = "/data/code/all_ws/ws/csv"
    # 遍历整个文件夹 打包在在3个小时区间的文件
    odom_folder_list = [os.path.join(csv_path, i) for i in os.listdir(csv_path)]
    csv_list = []
    VDR_list = []
    for file in odom_folder_list:
        # vdr是文件 单独处理
        if os.path.isdir(file):
            # 判断vdr文件夹最后修改的时间
            if abs(os.stat(file).st_mtime - target_timestamp) < 60 * 60 * 12:
                VDR_list.append(file)

        # trajectory_conversion开头的
        if file.split("/")[0].startswith("trajectory_conversion"):
            # 0.5h
            if abs(os.stat(file).st_mtime - target_timestamp) < 60 * 60 * 0.5:
                csv_list.append(file)
        else:
            if abs(os.stat(file).st_mtime - target_timestamp) < 60 * 60 * 12:
                csv_list.append(file)

    save_log_path = os.path.join(SAVE_LOG_PATH, "csv")
    # 打包过滤出的日志文件
    save_file(save_log_path, csv_list[:10])
    print("csv pack ok")


def pack_keep_error_event_process():
    """
    打包keep_error_event文件, 就一个文件
    /data/code/all_ws/ws/igv_log/keeper_error_event.log
    :return:
    """
    keeper_error_event_path = "/debug/igv_log/keeper_error_event.log"
    save_path = os.path.join(SAVE_LOG_PATH, "keeper_error_event")
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_file(save_path, [keeper_error_event_path, ])
    # subprocess.getoutput('cp ' + keeper_error_event_path + ' ' + SAVE_LOG_PATH)


def pack_odom_process(target_timestamp, intervals_timestamp=60 * 60 * 1):
    """
    打包odom文件
    odom日志内部自己分了以日切分的文件夹 2022-05-29_21-43-28
    先确定文件夹，再文件夹中筛选
    :return:
    """
    try:
        odom_path = "/data/key_log/odom"
        # 遍历整个文件夹 打包在在3个小时区间的文件
        odom_folder_list = [os.path.join(odom_path, i) for i in os.listdir(odom_path)]
        need_folder_list = []
        save_odom_file_list = []
        # 文件夹的筛选 最后修改的时间的文件夹
        for folder in odom_folder_list:
            if abs(os.stat(folder).st_mtime - 60 * 60 * 6) < target_timestamp:
                need_folder_list.append(folder)
        # ['/data/key_log/odom/2022-05-29_23-02-17', '/data/key_log/odom/2022-05-29_21-43-28', '/data/key_log/odom/2022-05-24_08-11-30']
        all_odom_file_list = []
        # 筛选出来的文件组装列表
        for need_folder in need_folder_list:
            item_list = [os.path.join(need_folder, i) for i in os.listdir(need_folder)]
            all_odom_file_list.extend(item_list)
        final_list = []
        # 过滤时间半小时以内的
        for file in all_odom_file_list:
            if abs(os.stat(file).st_mtime - target_timestamp) < 60 * 60 * 0.5:
                final_list.append(file)
        save_log_path = os.path.join(SAVE_LOG_PATH, "odom")
        # 打包过滤出的日志文件
        save_file(save_log_path, final_list)
        print("odom pack ok")
    except Exception as e:
        print(e)


def pack_lidar_process(target_timestamp, intervals_timestamp=60 * 60 * 0.5):
    """
    打包lidar文件 0.5h
    /data/key_log/lidar 目录下是根据时间戳区分了文件夹
    :return:
    """
    # 遍历整个文件夹 打包在在半个小时区间的文件
    lidar_path = "/data/key_log/lidar"
    lidar_folder_list = [os.path.join(lidar_path, i) for i in os.listdir(lidar_path)]
    save_lidar_folder_list = []
    for lidar_folder in lidar_folder_list:
        if abs(int(lidar_folder.split("/")[-1].strip()) - target_timestamp) < intervals_timestamp:
            save_lidar_folder_list.append(lidar_folder)

    save_log_path = os.path.join(SAVE_LOG_PATH, "lidar")
    # 打包过滤出的日志文件
    save_file(save_log_path, save_lidar_folder_list)

    print("pack_lidar ok")



def pack_supervisord_log_process(target_timestamp):
    """
    打包supervisord_log文件
    过滤出重要的 agent alignment_planner function_controller keeper landmark_localizer_ros2 lidar_estop
               lidar_preprocess  local_plan mqtt_adaptor qomolo_assembly vehicle_controller
    :return:
    """
    need_str_list = ["agent", "alignment_planner", "function_controller", "keeper", "landmark_localizer_ros2",
                     "lidar_estop", "lidar_preprocess", "local_plan", "mqtt_adaptor", "qomolo_assembly",
                     "vehicle_controller"]
    supervisord_path = "/debug/igv_log"
    supervisord_file_list = [os.path.join(supervisord_path, i) for i in os.listdir(supervisord_path)]
    save_supervisord_file_list = []
    for file in supervisord_file_list:
        # "/data/code/all_ws/ws/igv_log/lidar_estop.log.1-2022-05-22-23-1518.log" 取出lidar_estop
        if file.split(".")[0].split("/")[-1] in need_str_list:
            if abs(os.stat(file).st_mtime - target_timestamp) < 60 * 60 * 6:
                save_supervisord_file_list.append(file)
    save_log_path = os.path.join(SAVE_LOG_PATH, "supervisord")
    # 打包过滤出的日志文件
    save_file(save_log_path, save_supervisord_file_list)

    print("pack_supervisord ok")


def pack_git_repos_procrss():
    """
    打包git信息
    /opt/qomolo/qpilot/qpilot.repos
    :return:
    """
    save_log_path = SAVE_LOG_PATH
    target_file = ["/opt/qomolo/qpilot/qpilot.repos", ]
    save_file(save_log_path, target_file)
    print("pack_git_repos ok")


def gzip_file(SAVE_LOG_PATH, SAVE_FILE_NAME):
    """
    压缩文件夹为tar.gz包
    :param SAVE_LOG_PATH:
    :return:
    """
    print("start gzip ")
#    cmd_str = 'tar -cvzf ' + SAVE_FILE_NAME + ' ' + SAVE_LOG_PATH
    bag_name =  SAVE_LOG_PATH.split("/")[-1]
    cmd_str = "cd /debug/logpush_tmp/tmp && tar -zcvf " + SAVE_FILE_NAME  + " " + bag_name
    print("cmd:{}".format(cmd_str))
    subprocess.getoutput(cmd_str)
    print("gzip ok")


def upload(file_path):
    transport = paramiko.Transport(HOST, PORT)
    transport.connect(username=USERNAME, password=PASSWORD)
    sftp = paramiko.SFTPClient.from_transport(transport)
    # 生成上传目录
    YEAR = str(datetime.datetime.now().year)
    MONTH = str(datetime.datetime.now().month)
    DAY = str(datetime.datetime.now().day)
    YEAR_PATH = ROOT_PATH + "/" + YEAR
    MONTH_PATH = YEAR_PATH + "/" + MONTH
    DAY_PATH = MONTH_PATH + "/" + DAY
    ID_PATH = DAY_PATH + "/" + QOMOLO_ROBOT_ID

    year_existence = True if YEAR in sftp.listdir(ROOT_PATH) else False
    if not year_existence:
        sftp.mkdir(YEAR_PATH)
    month_existence = True if MONTH in sftp.listdir(YEAR_PATH) else False
    if not month_existence:
        sftp.mkdir(MONTH_PATH)
    day_existence = True if DAY in sftp.listdir(MONTH_PATH) else False
    if not day_existence:
        sftp.mkdir(DAY_PATH)
    id_existence = True if QOMOLO_ROBOT_ID in sftp.listdir(DAY_PATH) else False
    if not id_existence:
        sftp.mkdir(ID_PATH)

    file_name = os.path.basename(file_path)
    remote_path = ID_PATH + "/" + file_name
    print("file_path :{} remote_path: {}".format(file_name, remote_path))
    file_size = os.stat(file_path).st_size
    print("要上传的压缩包大小: {} ".format(size_format(file_size)))
    try:
        print("start upload.....")
        sftp.put(file_path, remote_path)
        print("upload success")
        return remote_path
    except:
        return None


def get_remote_path(file_path):
    """
    生成远程上传目录
    :return:
    """
    # 生成上传目录
    YEAR = str(datetime.datetime.now().year)
    MONTH = str(datetime.datetime.now().month)
    DAY = str(datetime.datetime.now().day)
    YEAR_PATH = ROOT_PATH + "/" + YEAR
    MONTH_PATH = YEAR_PATH + "/" + MONTH
    DAY_PATH = MONTH_PATH + "/" + DAY
    ID_PATH = DAY_PATH + "/" + QOMOLO_ROBOT_ID
    file_name = os.path.basename(file_path)
    remote_path = ID_PATH + "/" + file_name
    print("远程目录地址： {}".format(remote_path))
    return remote_path


def time_str_to_int(time_str_input):
    time_str = time_str_input[0:4] + "-" + time_str_input[4:6] + "-" + time_str_input[6:8] + \
               " " + time_str_input[9:11] + ":" + time_str_input[11:13] + ":" + time_str_input[13:15]
    if re.match(r'(.*)-(.*)-(.*) (.*):(.*):(.*)', time_str) != None and len(time_str) == 19:
        float_time = time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S'))
        int_time_stamp = int(float_time)
        return int_time_stamp
    else:
        return "timestamp format wrong"


def qlog_search(QLOG_PATH, log_folder_path, problem_time_int):
    agent_log_list = os.listdir(QLOG_PATH)
    error_list = []
    warning_list = []
    result_list = []
    info_list = []
    for item in agent_log_list:
        if "WARNING" in item and len(item) > 50:
            warning_list.append(item)
        if "INFO" in item and len(item) > 50:
            info_list.append(item)
        if "ERROR" in item and len(item) > 50:
            error_list.append(item)
    warning_list.sort()
    error_list.sort()
    info_list.sort()
    for i in range(0, len(info_list) - 1):
        # print(info_list[i].split(".")[5])
        if time_str_to_int(info_list[i].split(".")[5]) < problem_time_int and time_str_to_int(
                info_list[i + 1].split(".")[5]) > problem_time_int:
            result_list.append(QLOG_PATH + info_list[i - 2])
            result_list.append(QLOG_PATH + info_list[i - 1])
            result_list.append(QLOG_PATH + info_list[i])
            if len(result_list) >= (i + 1):
                result_list.append(QLOG_PATH + info_list[i + 1])
            if len(result_list) >= (i + 2):
                result_list.append(QLOG_PATH + info_list[i + 2])
    for i in range(0, len(error_list) - 1):
        if time_str_to_int(error_list[i].split(".")[5]) < problem_time_int and time_str_to_int(
                error_list[i + 1].split(".")[5]) > problem_time_int:
            result_list.append(QLOG_PATH + error_list[i - 2])
            result_list.append(QLOG_PATH + error_list[i - 1])
            result_list.append(QLOG_PATH + error_list[i])
            if len(result_list) >= (i + 1):
                result_list.append(QLOG_PATH + error_list[i + 1])
            if len(result_list) >= (i + 2):
                result_list.append(QLOG_PATH + error_list[i + 2])
    for i in range(0, len(warning_list) - 1):
        if time_str_to_int(warning_list[i].split(".")[5]) < problem_time_int and time_str_to_int(
                warning_list[i + 1].split(".")[5]) > problem_time_int:
            result_list.append(QLOG_PATH + warning_list[i - 2])
            result_list.append(QLOG_PATH + warning_list[i - 1])
            result_list.append(QLOG_PATH + warning_list[i])
            if len(result_list) >= (i + 1):
                result_list.append(QLOG_PATH + warning_list[i + 1])
            if len(result_list) >= (i + 2):
                result_list.append(QLOG_PATH + warning_list[i + 2])
    for file in result_list:
        src_path = file
        dst_path = log_folder_path + "/qlog/" + file.split("/")[-1]
        print(dst_path)
        shutil.copyfile(src_path, dst_path)


def pre_log_search():
    now_time = time.strftime('%Y-%m-%d-%H%M%S', time.localtime(time.time() + 28800)) + "_log_bag"
    log_folder_path = "/debug/logpush_tmp/tmp/" + QOMOLO_ROBOT_ID + "_" + now_time
    os.makedirs(log_folder_path + "/" + "localization_bag")
    os.makedirs(log_folder_path + "/" + "lidar_estop_bag")
    os.makedirs(log_folder_path + "/" + "odom_bag")
    os.makedirs(log_folder_path + "/" + "csv")
    os.makedirs(log_folder_path + "/" + "supervisord_log")
    os.makedirs(log_folder_path + "/" + "qlog")
    return log_folder_path


def pack_rosbag_process(id_list):
    """
    录制ros 数据包
    :param id_list:
    :return:
    """
    print("录制类型id: {}".format(id_list))
    for modul_id in id_list:
        pack_rosbag_by_id(modul_id)


def pack_rosbag_by_id(modul_id, record_time=None):
    """
    录制rog包数据，有感知数据包，规划数据包
    subprocess.Popen开启子进程返回pid  间隔一段时间后kill掉
    """
    print("开始录制ros bag！")
    print("QOMOLO_ROBOT_ID : {}".format(QOMOLO_ROBOT_ID))
    if modul_id == 2:
        # 录定位数据包
        ros_bag_cmd = "ros2 bag record /clock /{0}/odom /{0}/gnss/odom /{0}/localization/odom /{0}/full_pointcloud".format(QOMOLO_ROBOT_ID)
        modul_name = "localization"
    elif modul_id == 3:
        # 录感知数据包
        ros_bag_cmd = "ros2 bag record /{0}/tf /{0}/tf_static /{0}/lidar_estop_viz /{0}/odom /{0}/gnss/odom /{0}/livox/front_mid /{0}/livox/front_left /{0}/livox/front_right1 /{0}/livox/front_right2 /{0}/livox/rear_mid /{0}/livox/rear_right /{0}/livox/rear_left1 /{0}/livox/rear_left2 /{0}/pandar/front_left /{0}/pandar/front_right /{0}/pandar/rear_left /{0}/pandar/rear_right /rslidar_points/front /rslidar_points/rear /{0}/lidar_preprocess/wheelbox /{0}/filtered_pointcloud".format(QOMOLO_ROBOT_ID)
        modul_name = "perception"
    elif modul_id == 4:
        # 录规划数据包
        ros_bag_cmd = "ros2 bag record /{0}/tf /{0}/tf_static /{0}/odom /{0}/localization/odom /{0}/filtered_pointcloud /{0}/local_plan_new /{0}/planning_debug".format(QOMOLO_ROBOT_ID)
        modul_name = "planning"
    elif modul_id == 5:
        # 录规划数据包
        ros_bag_cmd = "ros2 bag record /clock /{0}/odom /{0}/gnss/odom".format(QOMOLO_ROBOT_ID)
        modul_name = "odom"
    else:
        print("不支持的类型")
        return False
    source_ros = "source /opt/qomolo/qpilot/setup.bash"
    cmd_str =("{} && {}". format(source_ros, ros_bag_cmd))
    print("运行的指令:{}".format(cmd_str))
    # 开启子进程
    process_pid = subprocess.Popen(cmd_str, shell=True).pid
    # 暂时写死1min
    time.sleep(int(10))
    # 停止进程
    kill_cmd = 'echo nvidia | sudo -S kill -9 {}'.format(process_pid)
    print("kill_cmd :{}".format(kill_cmd))
    subprocess.getoutput(kill_cmd)
    time.sleep(1)
    # os.kill(process_pid, signal.SIGTERM)
    bag_folder = subprocess.getoutput('ls /debug/rosbag* -dt | head -n 1')
    # 获取压缩包
    bag_path = os.path.join("/debug", bag_folder)
    print("已经录制成功的数据路径：{}".format(bag_path))
    # 上传打包好的文件包到打包目录下
    save_log_path = os.path.join(SAVE_LOG_PATH, "ros_bag", modul_name)
    # 打包过滤出的日志文件
    save_file(save_log_path, [bag_folder,])


def pack_and_push_log(problem_time_int, SAVE_FILE_NAME, log_type_id_list):
    """
    打包和push到nas服务器上
    :param problem_time_int:
    :param SAVE_FILE_NAME:
    :param type_id_list:
    :return:
    """
    if 1 in log_type_id_list:
        # 打包Qlog
        print("1. 打包Qlog")
        pack_Qlog_process(problem_time_int)

        # 打包keep_error_event
        print("2. 打包keep_error_event")
        pack_keep_error_event_process()

        # 打包odom
        print("3. 打包odom")
        pack_odom_process(problem_time_int)

        # 打包lidar
        print("4. 打包lidar")
        pack_lidar_process(problem_time_int)

        # 打包supervisord_log
        print("5. 打包supervisord_log")
        pack_supervisord_log_process(problem_time_int)

        # 包csv
        print("6. 打包csv")
        pack_csv_process(problem_time_int)

    print("7. 打包git repos")
    pack_git_repos_procrss()

    print("8. ros topic 录数据")
    pack_rosbag_process(log_type_id_list)

    print("9. 开始压缩")
    gzip_file(SAVE_LOG_PATH, SAVE_FILE_NAME)

    print("10. 上传压缩包")
    ret_upload = upload(SAVE_FILE_NAME)

    print("LOG 处理完成")
    return ret_upload


def size_format(b):
    """
    size单位转换
    :param b: bit单位
    :return:
    """
    if b < 1000:
        return '%i' % b + 'B'
    elif 1000 <= b < 1000000:
        return '%.1f' % float(b / 1000) + 'KB'
    elif 1000000 <= b < 1000000000:
        return '%.1f' % float(b / 1000000) + 'MB'
    elif 1000000000 <= b < 1000000000000:
        return '%.1f' % float(b / 1000000000) + 'GB'
    elif 1000000000000 <= b:
        return '%.1f' % float(b / 1000000000000) + 'TB'


def check_env_parameter():
    """
    检查必须的地面站服务器相关参数
    :return:
    """
    cmd = "source /opt/qomolo/utils/qomolo_gcs_scripts/log/env && echo $QOMOLO_ROBOT_ID"
    ROBOT_ID = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                shell=True, executable='/bin/bash').stdout.read().decode().strip("\n").strip()
    print("ROBOT_ID: ", ROBOT_ID)
    if not ROBOT_ID:
        print("QOMOLO_ROBOT_ID 参数缺失 请检查添加")
        return False, "QOMOLO_ROBOT_ID"
    else:
        global QOMOLO_ROBOT_ID
        QOMOLO_ROBOT_ID = ROBOT_ID
        return True, None



app = Flask(__name__)

test_response = {
    "result": "success"
    }

#QOMOLO_ROBOT_ID + "/path_convert"
@app.route("/downstream/set_path_convert", methods = ['POST'])
def set_path_convert():
    msg_data = String()
    msg = request.get_json()
    msg_data.data = json.dumps(msg)
    ros2_node.publisher_path_convert.publish(msg_data)
    return test_response

#QOMOLO_ROBOT_ID + '/function_control/ext/request'  //  QOMOLO_ROBOT_ID + 'function_control/set_bcm'
@app.route('/downstream/set_request', methods = ['POST'])
def set_request():
    msg1 = SetBcm.Request()
    data = request.get_json()
    msg = UInt8()
    msg.data = data["request"]
    msg1_data = int(msg.data)
    if msg1_data == int("6") or msg1_data == int("7"):
        msg1.request = int(msg1_data) + int("4")
        ros2_node.future = ros2_node.cli.call_async(msg1) 
    else:
        ros2_node.pub_func_request.publish(msg)

    print("set_request: ", data["request"])
    return test_response

#QOMOLO_ROBOT_ID + '/agent/ext/request'
@app.route('/downstream/set_task_request', methods = ['POST'])
def set_task_request():
    data = request.get_json()
    msg = UInt8()
    msg.data = data["request"]
    ros2_node.pub_task_request.publish(msg)
    print("set_task_request: ", data["request"])
    return test_response

#QOMOLO_ROBOT_ID + '/goal_pose' 
@app.route('/downstream/set_goal_pose', methods = ['POST'])
def set_goal_pose():
    data = request.get_json()
    msg = PoseStamped()
    msg.header.stamp = ros2_node.get_clock().now().to_msg()
    msg.header.frame_id = "map"
    msg.pose.position.x = data["x"]
    msg.pose.position.y = data["y"]
    msg.pose.position.z = data["z"]
    msg.pose.orientation = ros2_node.quaternion_from_yaw(data["heading"])
    ros2_node.pub_goal_pose.publish(msg)
    print("set_goal_pose x: %.2f, y: %.2f, z: %.2f, heading: %.2f"%(data["x"], data["y"], data["z"], data["heading"]))
    return test_response

#QOMOLO_ROBOT_ID + '/initialpose
@app.route('/downstream/set_initial_pose', methods = ['POST'])
def set_goal():
    data = request.get_json()
    msg = PoseWithCovarianceStamped()
    msg.header.stamp = ros2_node.get_clock().now().to_msg()
    msg.header.frame_id = "map"
    msg.pose.pose.position.x = data["x"]
    msg.pose.pose.position.y = data["y"]
    msg.pose.pose.position.z = data["z"]
    msg.pose.pose.orientation = ros2_node.quaternion_from_yaw(data["heading"])
    ros2_node.pub_initial_pose.publish(msg)
    print("set_initial_pose x: %.2f, y: %.2f, z: %.2f, heading: %.2f"%(data["x"], data["y"], data["z"], data["heading"]))
    return test_response


#QOMOLO_ROBOT_ID + '/container_operation'
@app.route('/downstream/asc/set_spreader_operation', methods = ['POST'])
def set_spreader_opertaion_request():
     data = request.get_json()
    
     cmd = data.get("cmd", 0)
     print("set_spreader_operation_request, cmd: %d"%cmd)

     if cmd == 2:
         if not ros2_node.container_operation_state.server_state:
             print("Not canceling task, container server is not running")
             return test_response_failure
         ros2_node.spreader_action_client.cancel_goal()
         return test_response_success
     elif cmd == 1:
         if ros2_node.container_operation_state.server_state:
             print("Not sending task, container server is running")
             return test_response_failure
     else:
         print("Invalid 'cmd'")
         return test_response_failure

     goal = ContainerOperation.Goal()
     goal.id = data.get("id", "")
     if goal.id == "":
         return test_response_failure

     goal.op = data.get("op", 0)
     if goal.op == 0:
         return test_response_failure

     goal.tier = data.get("tier", 0)
     if goal.tier is None:
         return test_response_failure

     goal.size = data.get("size", 0)
     if goal.size is None:
         return test_response_failure

     goal.area = data.get("area", 0)
     if goal.area is None:
         return test_response_failure

     goal.ctnr_height = data.get("ctnr_height", 2.591)
     goal.work_height = data.get("work_height", 11.9)
     goal.height = data.get("height", 11.9)
     goal.front_hydr = data.get("front_hydr", 0.35)
     goal.back_hydr = data.get("back_hydr", 0.35)
     goal.twistlock = data.get("twistlock", False)
     ros2_node.spreader_action_client.send_goal(goal)

     print("Send goal, op: %d, id: %s"%(goal.op, goal.id))
     print("size: %d, tier: %d, area: %d"%(goal.size, goal.tier, goal.area))
     print("ctnr_height: %.3f, work_height: %.3f"%(goal.ctnr_height, goal.work_height))
     print("front_hydr: %.3f, back_hydr: %.3f, height: %.3f"%(goal.front_hydr, goal.back_hydr, goal.height))
     print("twistlock: %d"%goal.twistlock)

     return test_response_success



@app.route("/logpush", methods=['GET', 'POST'])
def log_push():
    """
    获取打包上传日志
    :return:
    """
    try:
        global SAVE_LOG_PATH
        SAVE_LOG_PATH = SAVE_LOG_PATH_NEW
        now_time = time.strftime("%Y-%m-%d-%H-%M", time.localtime(time.time()))
        # 保存log的目录
        SAVE_LOG_PATH = SAVE_LOG_PATH + "_" + now_time + "_log_bag"
        # 压缩包的名字
        SAVE_FILE_NAME = SAVE_LOG_PATH.split("/")[-1] + ".tar.gz"
        # 保存压缩包的位置：/data/code/all_ws/ws/logpush_tmp/tmp/xxx.tar.gz
        SAVE_FILE_PATH = os.path.join(SAVE_LOG_PATH, SAVE_FILE_NAME)
        """
        SAVE_LOG_PATH:/data/code/all_ws/ws/logpush_tmp/tmp/TJ_IGV_21_2022-06-02-16-19_log_bag
        SAVE_FILE_NAME:TJ_IGV_21_2022-06-02-16-19_log_bag.tar.gz
        SAVE_FILE_PATH:/data/code/all_ws/ws/logpush_tmp/tmp/TJ_IGV_21_2022-06-02-16-19_log_bag/TJ_IGV_21_2022-06-02-16-19_log_bag.tar.gz
        """
        print("SAVE_LOG_PATH:{}  \n SAVE_FILE_NAME:{} \n SAVE_FILE_PATH:{}".format(SAVE_LOG_PATH,
                                                                                   SAVE_FILE_NAME, SAVE_FILE_PATH))
        # 检查必要的参数
        check_flag, error_str = check_env_parameter()
        if not check_flag:
            ret_data = {
                "data": "parameter {}  missing , please check".format(error_str)
            }
            return jsonify(ret_data)

        if request.method == "POST":
            print("接口请求时间点： ", str(datetime.datetime.now()))

            if request.content_type.startswith('application/json'):
                print('application/json')
                problem_time = request.json.get('problem_time')
                log_type_id_list = request.json.get('log_type_id_list')
            elif request.content_type.startswith('multipart/form-data'):
                print('multipart/form-data')
                problem_time = request.form.get('problem_time')
                log_type_id_list = request.form.get('log_type_id_list')
            else:
                problem_time = request.values.get("problem_time")
                log_type_id_list = request.values.get("log_type_id_list")

            problem_time_int = int(time.mktime(time.strptime(problem_time, '%Y-%m-%d %H:%M:%S')))
            print("指定问题时间点:{}  ros数据包录制id列表:{}".format(problem_time, log_type_id_list))
            # 异步开启处理 开始打包push过程
            t_push = threading.Thread(target=pack_and_push_log, args=(problem_time_int, SAVE_FILE_PATH, log_type_id_list))
            t_push.daemon = True
            t_push.start()

            ret = get_remote_path(SAVE_FILE_PATH)
            if ret:
                ret_data = {
                    "data": ret
                }
            else:
                ret_data = {
                    "data": "error"
                }
            return jsonify(ret_data)

        if request.method == "GET":
            # 测试用
            print(str(datetime.datetime.now()) + "——" + "logpush")
            qlog_list = ["agent", "canbus", "control", "function_control", "keeper", "planning", "perception",
                         "localization"]
            # 测试用当前时间戳
            problem_time_int = int(time.time())
            # problem_time_int = 1653831825 2022-05-29 21:43:45
            # 转成时间戳
            # problem_time = request.args.get('problem_time_int')
            # problem_time_int = int(time.mktime(time.strptime(problem_time, '%Y-%m-%d %H:%M:%S')))
            # 开始打包push过程
            # ret = pack_and_push_log(problem_time_int, SAVE_FILE_PATH)
            type_id_list = request.args.get('log_type_id_list').split(",")
            type_id_list = [int(i) for i in type_id_list]
            print("指定时间点:{}  类型列表:{}".format(problem_time_int, type_id_list))
            # 异步开启处理
            t_push = threading.Thread(target=pack_and_push_log, args=(problem_time_int, SAVE_FILE_PATH, type_id_list))
            t_push.daemon = True
            t_push.start()
            ret = get_remote_path(SAVE_FILE_PATH)
            if ret:
                ret_data = {
                    "data": ret
                }
            else:
                ret_data = {
                    "data": "error"
                }
            return jsonify(ret_data)

    except Exception as e:
        print("logPush error:{}".format(e))
        ret_data = {
            "data": "error: {}".format(e)
        }
        return jsonify(ret_data)


@app.route("/ros_bag_record", methods=['GET', 'POST'])
def ros_bag_record():
    """
    指定时间 录制ros bag
    {
    "id": 2 //模式的id  2：录定位数据包  3：录感知数据包  4：录规划数据包
    "duration": 100 // 录制时长 单位秒
    }
    """
    try:
        check_flag, error_str = check_env_parameter()
        if not check_flag:
            ret_data = {
                "data": "parameter {}  missing , please check".format(error_str)
            }
            return jsonify(ret_data)

        if request.method == "POST":
            print("请求: " + str(datetime.datetime.now()) + "——" + "logpush")

            if request.content_type.startswith('application/json'):
                print('application/json')
                model_id = request.json.get('id')
            elif request.content_type.startswith('multipart/form-data'):
                print('multipart/form-data')
                model_id = request.json.get('id')
                duration = request.json.get('duration')
            else:
                model_id = request.json.get('id')
                duration = request.json.get('duration')



    except Exception as e:
        print("logPush error:{}".format(e))
        ret_data = {
            "data": "error: {}".format(e)
        }
        # IS_WORKING_FLAG = False
        return jsonify(ret_data)
