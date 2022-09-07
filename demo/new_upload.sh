#!/bin/bash 

#
#   针对 logpush 进行优化
#


#  文件与文件夹进行区分
#    文件：  
#           csv 文件：trajectory_conversion + igv_speed_lon_controller + igv_nlfb_lat_controller + alignment_log +  inposition_log  + lattice_planner \
#                     planning_trajectorys + planning_vehicle_state 
#                            -》 /data/code/all_ws/ws/csv  《-
#           .log文件：
#                    独立文件: keeper_error_event.log    
#                                  -》  /data/code/all_ws/ws/igv_log/ 《-
#                    各个模块的log: function_controller / mqtt_adaptor / mono_lane_tracker_ros2 / canbus / local_plan / localization_checker / vehicle_controller / \
#                                    qomolo_assembly / alignment_planner / agent / keeper / landmark_localizer_ros2 / lidar_estop  / planning / perception / \
#                                    control / localization_adaptor /gnss_driver / gnss_processor / hesai_lidar_4in1 / http_bridge / lidar_config_check / \
#                                    lidar_preprocess / localization_logger / vehicle_data_recorder / wheel_odom 
#                                     --> history  /data/code/all_ws/ws/igv_log  <--
#                                     --> real time /data/code/all_ws/ws/        <--
#            rosbag : odom      --> /data/key_log/ <-- 
#                    : lidar     --> /data/key_log/ <--
#
#    文件夹:
#            vdr 系列:  *vdr* / *localization* / *lidar_cps*   --> /data/code/all_ws/ws/csv/short_time <--
#            images :    *2022*            --> /data/code/all_ws/ws/key_log/image <--                (xm)               

#      qlog: 
#                   agent /  planning / perception / canbus / control / keeper / function_control / localization
#                                           --> /data/code/all_ws/ws/qlog <--

#    env 
#    文件必须设置为绝对路径 适配所有项目
#    CSV_PATH="/data/code/all_ws/ws/csv"
#    IGV_LOG_PATH="/data/code/all_ws/ws/igv_log"
#    LOCALIZATION_BAG_PATH="/data/key_log/"
#    "/data/code/all_ws/ws/csv/short_time"
#    "/data/code/all_ws/ws/key_log/image/"     (xm独有)

# 空间检查：   < 80G 不可执行logpush 

source /opt/qomolo/utils/qomolo_gcs_scripts/log/env

beijing_date_mark=""
if [[ ${QOMOLO_ROBOT_ID} == "" ]];then
    echo -e "\033[31m必须配置QOMOLO_ROBOT_ID\033[0m"
    exit 0
fi
if [[ ${GCS_PASSWORD} == "" ]];then
    echo -e "\033[31m必须配置地面站密码\033[0m"
    exit 0
fi
if [[ ${GCS_USERNAME} == "" ]];then
    echo -e "\033[31m必须配置地面站用户名\033[0m"
    exit 0
fi
if [[ ${GCS_IP} == "" ]];then
    echo -e "\033[31m必须配置地面站IP\033[0m"
    exit 0
fi
disk_len=`df -h | grep /data| grep -v docker | awk '{print $4}'  | cut -f 1 -d "G"`
if [[ "$disk_len" -lt "80" ]];then
    echo "请停止操作，检查磁盘大小，容量已经低于80G"
    exit 0
fi

# 修改文件所有者
sudo chown -R nvidia /data/code/all_ws/ws

read -p " 日志上传 1:
" MODE
read -p "speed mode:" speed

function speed_mode()
{
      if [[ $speed == "no" ]];then
            speed_status="xargs -I {} rsync -azv --progress --bwlimit=1024" 
      else  
            speed_status="xargs -I {} rsync -azv --progress" 
      fi
}


workspace="/data/code/all_ws/ws"
BJ_TIME=`date -d "+8 hour" +%Y_%m_%d_%H%M%S`
function input_time_create_folder()
{
    mkdir -p ${workspace}/logpush_tmp
    read -p "请输入问题发生时的北京时间:" PROBLEM_TIME
    if [[ ${#PROBLEM_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-09-06 12:00:00"
        exit 0
    else
    UPLOAD_LOG_NAME=${HOSTNAME}-${BJ_TIME}_log_bag
    cd ${workspace}/logpush_tmp && sudo rm -rf *
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/lidar_estop_bag
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr 
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images              # xm
    fi
    TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP - 28801`           #8H
    UTC_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
}
# --》 20 《--
TIMESTAMP=`date -d "${UTC_TIME}" +%s`
TIMESTAMP_CHANGE=`expr $TIMESTAMP - 1200`           #40min
START_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
TIMESTAMP=`date -d "${UTC_TIME}" +%s`
TIMESTAMP_CHANGE=`expr $TIMESTAMP + 1200`          
END_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`


# --》 10 《--                                      
TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
TIMESTAMP_CHANGE=`expr $TIMESTAMP - 600`           #20min
start_time=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
TIMESTAMP_CHANGE=`expr $TIMESTAMP + 600`          
end_time=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`


# 高频搜索文件： 上下20分钟
function csv_high_search_copy()
{
    cd ${CSV_PATH}
    find ./ -name "$1*" -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv

}
# 低频搜索文件： 上下10分钟
function csv_low_search_copy()
{
    cd ${CSV_PATH}
    find ./ -name "$1*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {} speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}


#keeper_error_event
function log_keeper_error_event_search_copy()
{
    cd ${IGV_LOG_PATH}
    rsync -azv --progress keeper_error_event.log ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/
}

function log_history_search_copy()
{
    cd ${IGV_LOG_PATH}
    find ./ -name "$1*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
}

function log_real_time_search_copy()
{
    cd ${workspace}
    # find ./ -name "$1*" | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name function_controller* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name mqtt_adaptor* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name  mono_lane_tracker_ros2* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name canbus* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log 
    find ./ -name local_plan* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log 
    find ./ -name localization_checker* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log 
    find ./ -namevehicle_controller* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name qomolo_assembly* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name alignment_planner* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name agent* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name keeper*  | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name landmark_localizer_ros2* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name lidar_estop* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name lidar_preprocess* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name localization_logger* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name vehicle_data_recorder* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name wheel_odom* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name localization_adaptor*  | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name gnss_driver* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name gnss_processor* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name hesai_lidar_4in1*  | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name http_bridge* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find ./ -name lidar_config_check* | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
} 


#rosbag
function rosbag_lidar_bag_search_copy()
{
    cd ${LOCALIZATION_BAG_PATH}/lidar
    find ./ -name "1*"  -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} `$speed_status` {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/lidar 
}

function rosbag_localization_bag_search_copy()
{
    cd ${LOCALIZATION_BAG_PATH}/odom  
    find ./ -name "*.db3"  -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {}  `$speed_status` {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
}


#vdr
function vdr_search_copy()
{
    cd ${CSV_PATH}/short_time
    find ./ -name "*vdr*"  -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  $speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
    find ./ -name "*localization*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
    find ./ -name "*lidar_cps*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
}


#qlog
function qlog_all_search_copy()
{
      cd ${workspace}/qlog/$1
      mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
      find ./ -name "$1*" -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1/
}


#images
function images_sreach_copy_for_xm()
{
    cd ${workspace}/key_log/image
    find ./ -name "*2022*" -type d -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images
}

case "${MODE}" in 
1*)
## TJ - 天津
# if [[ ${HOSTNAME} =~ ^TJ ]];then
if [[ "${HOSTNAME}" =~ ^TJ_IGV.* ]];then
    input_time_create_folder
    #csv
    csv_high_search_copy trajectory
    csv_low_search_copy alignment_log
    csv_low_search_copy igv_nlfb_lat_controller
    csv_low_search_copy igv_speed_lon_controller
    csv_low_search_copy inposition_log
    csv_low_search_copy lattice_planner
    csv_low_search_copy planning_trajectorys
    csv_low_search_copy planning_vehicle_state
    #log
    log_keeper_error_event_search_copy
    log_history_search_copy function_controller
    log_history_search_copy mqtt_adaptor
    log_history_search_copy mono_lane_tracker_ros2
    log_history_search_copy canbus
    log_history_search_copy local_plan
    log_history_search_copy localization_checker
    log_history_search_copy vehicle_controller
    log_history_search_copy qomolo_assembly
    log_history_search_copy alignment_planner
    log_history_search_copy agent
    log_history_search_copy keeper 
    log_history_search_copy landmark_localizer_ros2
    log_history_search_copy lidar_estop
    log_history_search_copy lidar_preprocess
    log_history_search_copy localization_logger
    log_history_search_copy vehicle_data_recorder
    log_history_search_copy wheel_odom
    log_history_search_copy localization_adaptor 
    log_history_search_copy gnss_driver
    log_history_search_copy gnss_processor
    log_history_search_copy hesai_lidar_4in1 
    log_history_search_copy http_bridge
    log_history_search_copy lidar_config_check 
    # log_real_time_search_copy
    #rosbag
    rosbag_lidar_bag_search_copy
    rosbag_localization_bag_search_copy
    #vdr
    vdr_search_copy
    #qlog
    qlog_all_search_copy agent 
    qlog_all_search_copy planning 
    qlog_all_search_copy perception 
    qlog_all_search_copy canbus 
    qlog_all_search_copy control 
    qlog_all_search_copy keeper
    qlog_all_search_copy function_control 
    qlog_all_search_copy localization
fi
;;
esac