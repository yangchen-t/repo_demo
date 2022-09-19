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
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr 
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images              # xm
    fi
    TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP - 28801`           #8H
    SEARCH_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
}

function function_LOGPUSH_name(){
    cd /data/code/all_ws/ws/logpush_tmp
    sudo rm -rf tmp
    UPLOAD_LOG_NAME=${HOSTNAME}_`date -d "8 hour" +%Y-%m-%d-%H%M`_$1
    mkdir -p /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}
    cd /data/code/all_ws/ws
}



#  // CSV
# 高频率搜索文件： 上下4个文件
function csv_high_search_copy()
{
    cd /data/code/all_ws/ws/csv/
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 4 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv/
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 4 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv/
#     find ./ -name "$1*" -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv

}
# 低频搜索文件： 上下 2个文件
function csv_low_search_copy()
{
#     cd ${CSV_PATH}
#     find ./ -name "$1*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {} speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    cd /data/code/all_ws/ws/csv/
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv/
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv/
}



#  // LOG
#keeper_error_event
function log_keeper_error_event_search_copy()
{
    cd /data/code/all_ws/ws/igv_log
    rsync -azv --progress keeper_error_event.log ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/
}

#   上下 2个文件
function log_history_search_copy()
{
#     cd ${IGV_LOG_PATH}
    cd /data/code/all_ws/ws/igv_log
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
#     find ./ -name "$1*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
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

function log_real_time_search_copy->igv_log()
{
      cd /data/code/all_ws/ws/
      beijing_date_mark=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
      ls *.log | xargs -I  {} rsync -avz --progress   {}  /data/code/all_ws/ws/igv_log/{}-${beijing_date_mark}.log
}


# // ROSBAG 
#上下两个
function rosbag_lidar_bag_search_copy()
{
#     cd ${LOCALIZATION_BAG_PATH}/lidar
    cd /data/key_log/lidar
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
#     find ./ -name "1*"  -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} `$speed_status` {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/lidar 
}
# 上下两个
function rosbag_localization_bag_search_copy()
{
#     cd ${LOCALIZATION_BAG_PATH}/odom 
    cd /data/key_log/odom 
    oldder_csv=`find ./ -name "*$1" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
    newer_csv=`find ./ -name "*$1" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
#     find ./ -name "*.db3"  -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {}  `$speed_status` {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
}


#vdr
function vdr_search_copy()
{
#     cd ${CSV_PATH}/short_time
      cd /data/code/all_ws/ws/csv/short_time
      oldder_lidar=`find ./ -maxdepth 1 ! -path ./ -type d ! -newermt "${SEARCH_TIME}"`
      ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
      newer_lidar=`find ./ -maxdepth 1 ! -path ./ -type d -newermt "${SEARCH_TIME}"`
      ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
#     find ./ -name "*vdr*"  -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  $speed_status {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
#     find ./ -name "*localization*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
#     find ./ -name "*lidar_cps*" -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {}  speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
}


#  // qlog
# 上下两个
function qlog_all_search_copy()
{
      cd ${workspace}/qlog/$1
      mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
      oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
      ls -t ${oldder_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
      newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
      ls -rt ${newer_csv} | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
      # find ./ -name "$1*" -newermt "${start_time}" ! -newermt "${end_time}" | xargs -I {} speed_mode {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1/
}
#  // image 
# 上下3个 
function folder_search_lidar(){
    cd /data/key_log/lidar
    mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/lidar
    oldder_lidar=`find ./ -maxdepth 1 ! -path ./ -type d ! -newermt "${SEARCH_TIME}"`
    if [[ $oldder_lidar != "" ]];then
      ls -dt $oldder_lidar | head -n 5 |xargs  -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/lidar/
    fi
    newer_lidar=`find ./ -maxdepth 1 ! -path ./ -type d -newermt "${SEARCH_TIME}"`
    if [[ $newer_lidar != "" ]];then
      ls -drt $newer_lidar | head -n 5 |xargs  -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/lidar/
    fi
}

#images
# function images_sreach_copy_for_xm()
# {
#     cd ${workspace}/key_log/image
#     find ./ -name "*2022*" -type d -newermt "${START_TIME}" ! -newermt "${END_TIME}" | xargs -I {} rsync -azv --progress ${speed_down} {} ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images
# }
function upload_to_nas()
{
    rsync -avz --progress --bwlimit=1000     /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
    echo "=========================================以下数据正在被压缩========================================="
    cd /data/code/all_ws/ws/logpush_tmp/
    echo nvidia | sudo -S nice -n 19 tar -zvcf ${UPLOAD_LOG_NAME}.tar.gz ${UPLOAD_LOG_NAME}
    mkdir -p /data/code/all_ws/ws/logpush_nas/
    cp /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}.tar.gz /data/code/all_ws/ws/logpush_nas/
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%m`
    DAY=`date -d "8 hour" +%d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "========================================请把以下路径粘贴到issue==================================="
    echo ${UPLOAD_PATH}/${UPLOAD_LOG_NAME}.tar.gz
    echo "=================================================================================================="
}

function upload_to_gcs(){
    rsync -avz --progress --bwlimit=1000     /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/
    echo "=========================================以下数据正在被压缩========================================="
    cd /data/code/all_ws/ws/logpush_tmp/tmp/
    echo nvidia | sudo -S nice -n 19 tar -zvcf ${TMP_LOG_NAME}.tar.gz ${TMP_LOG_NAME}
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%m`
    DAY=`date -d "8 hour" +%d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "===========================================数据压缩已完成=========================================="
    echo "数据正在传输中......"
    sshpass -p ${GCS_PASSWORD} scp -l 8000 -o ServerAliveInterval=30 -o "StrictHostKeyChecking no" ${TMP_LOG_NAME}.tar.gz ${GCS_USERNAME}@${GCS_IP}:/key_log/key_log/
    if [ $? != 0 ];then
        echo -e "\033[031m数据因为网络原因传输失败，请联系管理员\033[0m"
        exit 0
    else
        echo "========================================请把以下路径粘贴到issue==================================="
        echo ${UPLOAD_PATH}/${TMP_LOG_NAME}.tar.gz
        echo "=================================================================================================="
    fi
}


case "${MODE}" in 
1*)
## TJ - 天津
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
    rosbag_localization_bag_search_copy .db3
    #vdr
    vdr_search_copy lidar
    vdr_search_copy localization
    #qlog
    qlog_all_search_copy agent 
    qlog_all_search_copy planning 
    qlog_all_search_copy perception 
    qlog_all_search_copy canbus 
    qlog_all_search_copy control 
    qlog_all_search_copy keeper
    qlog_all_search_copy function_control 
    qlog_all_search_copy localization
    #images

    upload_to_nas
fi
;;
esac