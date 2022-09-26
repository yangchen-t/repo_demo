#!/bin/bash

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

# read -p " 日志上传 1:
# " MODE

workspace="/data/code/all_ws/ws"
BJ_TIME=`date -d "+8 hour" +%Y_%m_%d_%H%M%S`
function input_time_create_folder()
{
    mkdir -p ${workspace}/logpush_tmp
    read -p "请输入问题发生时的北京时间:" PROBLEM_TIME
    echo `date` >> /data/code/all_ws/ws/.user_input_time_log
    echo $PROBLEM_TIME >> /data/code/all_ws/ws/.user_input_time_log
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
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images            # xm
    fi
    TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP - 28801`           #8H
    SEARCH_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
}

#keeper_error_event
function log_keeper_error_event_search_copy()
{
    cd /data/code/all_ws/ws/igv_log && rsync -azv --progress keeper_error_event.log ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/
}
function log_search_copy_pre()
{
    beijing_date=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    cd /data/code/all_ws/ws/
    ls *.log.* | xargs -I  {} cp {}  /data/code/all_ws/ws/igv_log/{}-${beijing_date}.log
}

function log_history_search_copy()
{
    find /data/code/all_ws/ws/igv_log/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find /data/code/all_ws/ws/igv_log/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
}
function csv_search_copy()
{
    find /data/code/all_ws/ws/csv/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    find /data/code/all_ws/ws/csv/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}
function high_csv_search_copy()
{
    find /data/code/all_ws/ws/csv/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    find /data/code/all_ws/ws/csv/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}
function qlog_all_search_copy()
{
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
    find /data/code/all_ws/ws/qlog/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
    find /data/code/all_ws/ws/qlog/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
}
function file_search_copy_odom()
{
    cd ${ODOM_FOLDER_NAME}
     oldder_odom=`find ./ -name "*.db3" ! -newermt "${SEARCH_TIME}"`
     if [[ $oldder_odom != "" ]];then
         ls -t $oldder_odom | head -n 5 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag/
     fi
     newer_odom=`find ./ -name "*.db3" -newermt "${SEARCH_TIME}"`
     if [[ $newer_odom != "" ]];then
         ls -rt $newer_odom | head -n 5 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag/
     fi
}
function vdr_search_copy()
{
    find /data/code/all_ws/ws/csv/short_time/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
    find /data/code/all_ws/ws/csv/short_time/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
}
function folder_search_lidar()
{
    cd /data/key_log/lidar
    # mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/lidar
    oldder_lidar=`find ./ -maxdepth 1 ! -path ./ -type d ! -newermt "${SEARCH_TIME}"`
    if [[ $oldder_lidar != "" ]];then
      ls -dt $oldder_lidar | head -n 5 |xargs  -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar/
    fi
    newer_lidar=`find ./ -maxdepth 1 ! -path ./ -type d -newermt "${SEARCH_TIME}"`
    if [[ $newer_lidar != "" ]];then
      ls -drt $newer_lidar | head -n 5 |xargs  -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar/
    fi
}
function folder_search_image()
{
    find /data/key_log/image/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
    find /data/key_log/image/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
}

function upload_to_nas()
{
    rsync -avz --progress   /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
    echo "=========================================以下数据正在被压缩========================================="
    cd /data/code/all_ws/ws/logpush_tmp/
    echo nvidia | sudo -S nice -n 19 tar -zvcf ${TMP_LOG_NAME}.tar.gz ${TMP_LOG_NAME}
    mkdir -p /data/code/all_ws/ws/logpush_nas/
    cp /data/code/all_ws/ws/logpush_tmp/${TMP_LOG_NAME}.tar.gz /data/code/all_ws/ws/logpush_nas/
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%m`
    DAY=`date -d "8 hour" +%d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "========================================请把以下路径粘贴到issue==================================="
    echo ${UPLOAD_PATH}/${TMP_LOG_NAME}.tar.gz
    echo "=================================================================================================="
}

function upload_to_gcs(){
    rsync -avz --progress /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${TMP_LOG_NAME}/
    echo "=========================================以下数据正在被压缩========================================="
    cd /data/code/all_ws/ws/logpush_tmp/
    echo nvidia | sudo -S nice -n 19 tar -zvcf ${TMP_LOG_NAME}.tar.gz ${TMP_LOG_NAME}
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%m`
    DAY=`date -d "8 hour" +%d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "===========================================数据压缩已完成=========================================="
    echo "数据正在传输中......"
    sshpass -p ${GCS_PASSWORD} scp -l 10000 -o ServerAliveInterval=30 -o "StrictHostKeyChecking no" ${TMP_LOG_NAME}.tar.gz ${GCS_USERNAME}@${GCS_IP}:/key_log/key_log/
    if [ $? != 0 ];then
        echo -e "\033[031m数据因为网络原因传输失败，请联系管理员\033[0m"
        exit 0
    else
        echo "========================================请把以下路径粘贴到issue==================================="
        echo ${UPLOAD_PATH}/${TMP_LOG_NAME}.tar.gz
        echo "=================================================================================================="
    fi
}


input_time_create_folder
log_search_copy_pre
sleep 5 
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
log_history_search_copy fusion
log_history_search_copy mono_lane_tracker_ros2
log_history_search_copy lidar_cps_alignment

#csv
high_csv_search_copy trajectory
csv_search_copy alignment
csv_search_copy igv_nlfb_lat_controlle
csv_search_copy igv_speed_lon_controller
csv_search_copy inposition_log
csv_search_copy lattice_planner
csv_search_copy planning_trajectorys
csv_search_copy planning_vehicle_state
#qlog
qlog_all_search_copy agent 
qlog_all_search_copy alignment_planner
qlog_all_search_copy vdr
qlog_all_search_copy planning 
qlog_all_search_copy perception 
qlog_all_search_copy canbus 
qlog_all_search_copy control 
qlog_all_search_copy keeper
qlog_all_search_copy function_control 
qlog_all_search_copy localization
#odom rosbag
file_search_copy_odom
#vdr
vdr_search_copy lidar
vdr_search_copy localization
# localization_lidar
folder_search_lidar
#images
folder_search_image 2022
#upload
upload_to_nas
