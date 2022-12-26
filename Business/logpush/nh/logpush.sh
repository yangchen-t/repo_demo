#!/bin/bash

source /opt/qomolo/utils/qomolo_gcs_scripts/log/env
source /opt/qomolo/utils/qpilot_setup/ws_supervisord/.env

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
if [[ ${NAS_PATH} == "" ]];then
    echo -e "\033[31m必须配置NAS路径\033[0m"
    exit 0
fi
if [[ ${CSV_FOLDER_NAME} == "" ]];then
    echo -e "\033[31m必须配置CSV路径\033[0m"
    exit 0
fi
if [[ ${ODOM_FOLDER_NAME} == "" ]];then
    echo -e "\033[31m必须配置odom路径\033[0m"
    exit 0
fi
disk_len=`df -h | grep /data| grep -v docker | awk '{print $4}'  | cut -f 1 -d "G"`
if [[ "$disk_len" -lt "80" ]];then
    echo "请停止操作，检查磁盘大小，容量已经低于80G"
    exit 0
fi

# 修改文件所有者
sudo chown -R nvidia /data/code/all_ws/ws

read -p "上传日志输入1:
录定位（凯爷+凌远+影姐）要的数据包输入2:
录感知（兵兵+家园+许宁）要的数据包输入3:
录碰撞误检（嘉俊）要的数据包输入4:
录制编码器航向角标定数据包输入5：
" MODE

workspace="/data/code/all_ws/ws"
BJ_TIME=`date -d "+8 hour" +%Y_%m_%d_%H%M%S`
function input_time_create_folder()
{
    mkdir -p ${workspace}/logpush_tmp
    read -p "请输入问题发生时的北京时间(例：2022-11-11 11:11:11):" PROBLEM_TIME
    echo `date` >> /data/code/all_ws/ws/.user_input_time_log
    echo $PROBLEM_TIME >> /data/code/all_ws/ws/.user_input_time_log
    if [[ ${#PROBLEM_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-09-06 12:00:00"
        exit 0
    else
    UPLOAD_LOG_NAME=${HOSTNAME}_${BJ_TIME}_log_bag
    sudo rm -r ${workspace}/logpush_tmp/*
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/vdr 
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/images           
    fi
    TIMESTAMP=`date -d "${PROBLEM_TIME}" +%s`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP - 28801`           #8H
    SEARCH_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
}

#tools
function bag_gen_folder()
{
    sudo rm -r ${workspace}/logpush_tmp/*
    UPLOAD_LOG_NAME=${HOSTNAME}_${BJ_TIME}_$1
    mkdir -p /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}
    cd /data/code/all_ws/ws
}
function log_search_copy_pre()
{
    beijing_date=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    cd /data/code/all_ws/ws/
    ls *.log* | xargs -I  {} cp {}  /data/code/all_ws/ws/igv_log/{}-${beijing_date}.log
}

function log_search_copy_post(){
    if [[ -d /data/code/all_ws/ws/igv_log ]];then
        rm /data/code/all_ws/ws/igv_log/*$beijing_date*
    else
        echo "igv_log not exist"
    fi
}

#keeper_error_event
function log_keeper_error_event_search_copy()
{
    cd /data/code/all_ws/ws/igv_log && rsync -azv --progress keeper_error_event.log ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/
}
function log_history_search_copy()
{
    find /data/code/all_ws/ws/igv_log/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 3 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find /data/code/all_ws/ws/igv_log/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 3 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
}
function csv_search_copy()
{
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}
function high_csv_search_copy()
{
    TIMESTAMP=`date -d "${SEARCH_TIME}" +%s`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP - 900`           #0.5H
    NEW_START_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
    TIMESTAMP_CHANGE=`expr $TIMESTAMP + 900`           #0.5H
    NEW_END_TIME=`date -d @$TIMESTAMP_CHANGE +%Y-%m-%d\ %H:%M:00`
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f  -newermt "${NEW_START_TIME}" ! -newermt "${NEW_END_TIME}" | grep $1 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}
function qlog_all_search_copy()
{
    cd 
    mkdir -p ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
    forward_list=`find /data/code/all_ws/ws/qlog/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | grep $2`
    if [[ $forward_list != "" ]];then
        ls -t $forward_list | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
    fi
    reverse_list=`find /data/code/all_ws/ws/qlog/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | grep $2`
    if [[ $reverse_list != "" ]];then
        ls -t $reverse_list | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/qlog/$1
    fi
}
function file_search_copy_odom()
{
    cd /data/key_log/odom
     oldder_odom=`find ./ -name "*.db3" ! -newermt "${SEARCH_TIME}"`
     if [[ $oldder_odom != "" ]];then
         ls -t $oldder_odom | head -n 5 | xargs -I {} rsync -avz --progress   {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag/
     fi
     newer_odom=`find ./ -name "*.db3" -newermt "${SEARCH_TIME}"`
     if [[ $newer_odom != "" ]];then
         ls -rt $newer_odom | head -n 5 | xargs -I {} rsync -avz --progress   {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_bag/
     fi
}
function vdr_search_copy()
{
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/short_time/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/short_time/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
}
function folder_search_lidar()
{
    find /data/key_log/lidar/* -type d ! -newermt "${SEARCH_TIME}" | tail -n 5 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
    find /data/key_log/lidar/* -type d  -newermt "${SEARCH_TIME}" | head -n 5 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar

}
function folder_search_image()
{
    find /data/key_log/image/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
    find /data/key_log/image/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
}

## other need 


###############################################################
function upload_to_nas()
{
    rsync -avz --progress  /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
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
    rsync -avz --progress  /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
    echo "=========================================以下数据正在被压缩========================================="
    cd /data/code/all_ws/ws/logpush_tmp/
    echo nvidia | sudo -S nice -n 19 tar -zvcf ${UPLOAD_LOG_NAME}.tar.gz ${UPLOAD_LOG_NAME}
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%m`
    DAY=`date -d "8 hour" +%d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "===========================================数据压缩已完成=========================================="
    echo "数据正在传输中......"
    sshpass -p ${GCS_PASSWORD} scp -l 10000 -o ServerAliveInterval=30 -o "StrictHostKeyChecking no" ${UPLOAD_LOG_NAME}.tar.gz ${GCS_USERNAME}@${GCS_IP}:/key_log/key_log/
    if [ $? != 0 ];then
        echo -e "\033[031m数据因为网络原因传输失败，请联系管理员\033[0m"
        exit 0
    else
        echo "========================================数据传输至地面站============================================"
        echo "/key_log/key_log/${UPLOAD_LOG_NAME}.tar.gz"
        echo "=================================================================================================="
    fi
}

function main()
{
    input_time_create_folder
    log_search_copy_pre
    sleep 5 
    #log
    log_keeper_error_event_search_copy
    log_history_search_copy agent
    log_history_search_copy assembly
    log_history_search_copy canbus
    log_history_search_copy container
    log_history_search_copy control
    log_history_search_copy function
    log_history_search_copy hesai_lidar_3in1
    log_history_search_copy keeper
    log_history_search_copy lidar_driver
    log_history_search_copy lidar_perception
    log_history_search_copy localization_adaptor
    log_history_search_copy localization_fuse
    log_history_search_copy localization_gnss
    log_history_search_copy localization_odom
    log_history_search_copy mqtt
    log_history_search_copy navigation
    log_history_search_copy safety_reporter 
    log_history_search_copy vdr
    log_history_search_copy voc
    log_history_search_copy image_visualization 
    log_history_search_copy spreader_camera_dl
    log_history_search_copy visual_perception

    sleep 2 

    #csv
    high_csv_search_copy trajectory
    csv_search_copy ws_lqr_lat
    csv_search_copy prediction_data 
    csv_search_copy velocity_position_longitudinal
    csv_search_copy first_level_safety
    csv_search_copy igv_nlfb_lat_controlle
    csv_search_copy igv_speed_lon_controller
    csv_search_copy lattice_planner
    csv_search_copy odom_log
    csv_search_copy planning_trajectorys
    csv_search_copy planning_vehicle_state

    sleep 2
    
    #qlog
    for i in ERROR WARNING INFO
    do
        qlog_all_search_copy agent $i
        qlog_all_search_copy alignment planner $i
        qlog_all_search_copy vdr $i
        qlog_all_search_copy planning $i
        qlog_all_search_copy perception $i
        qlog_all_search_copy canbus $i
        qlog_all_search_copy control $i
        qlog_all_search_copy keeper $i
        qlog_all_search_copy function_control $i
        qlog_all_search_copy localization $i
    done
    sleep 2
    #odom rosbag
    file_search_copy_odom
    #vdr
    vdr_search_copy lidar
    vdr_search_copy localization
    vdr_search_copy CO
    # localization_lidar
    #images
    folder_search_image 2022
    folder_search_lidar

}
#upload
case "$MODE" in
1*)
#天津
if [[ "${HOSTNAME}" =~ ^nh.* ]];then
    main
    upload_to_nas
elif [[ "${HOSTNAME}" =~ ^ctn* ]];then
    main
    upload_to_gcs
else 
    echo "所在项目不支持"
fi
;;
# 录定位数据包
2*)
bag_gen_folder localization_bag
docker exec -it qpilot bash -c "source /opt/qomolo/${ROS_WORKSPACE}/setup.bash &&  ros2 bag record /clock /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom /${QOMOLO_ROBOT_ID}/localization/odom /${QOMOLO_ROBOT_ID}/full_pointcloud"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress  /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
upload_to_nas
;;
# 录感知数据包
3*)
bag_gen_folder perception_bag
docker exec -it qpilot bash -c "source /opt/qomolo/${ROS_WORKSPACE}/setup.bash && ros2 bag record /${QOMOLO_ROBOT_ID}/tf /${QOMOLO_ROBOT_ID}/tf_static /${QOMOLO_ROBOT_ID}/lidar_estop_viz /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom /${QOMOLO_ROBOT_ID}/pandar/front_left /${QOMOLO_ROBOT_ID}/pandar/front_left_105 /${QOMOLO_ROBOT_ID}/pandar/rear_right_105 /${QOMOLO_ROBOT_ID}/pandar/front_right /${QOMOLO_ROBOT_ID}/pandar/rear_left /${QOMOLO_ROBOT_ID}/pandar/rear_right /rslidar_points/front /rslidar_points/rear /${QOMOLO_ROBOT_ID}/lidar_preprocess/wheelbox /${QOMOLO_ROBOT_ID}/filtered_pointcloud /${QOMOLO_ROBOT_ID}/localization/odom /${QOMOLO_ROBOT_ID}/straddle_carrier_visualiza /${QOMOLO_ROBOT_ID}/straddle_twistlock_points /${QOMOLO_ROBOT_ID}/chassis_state_feedback"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
upload_to_nas
;;
# 录规划数据包
4*)
bag_gen_folder collision_bag
docker exec -it qpilot bash -c "source /opt/qomolo/${ROS_WORKSPACE}/setup.bash &&  ros2 bag record /${QOMOLO_ROBOT_ID}/tf /${QOMOLO_ROBOT_ID}/tf_static /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/localization/odom /${QOMOLO_ROBOT_ID}/filtered_pointcloud /${QOMOLO_ROBOT_ID}/local_plan_new /${QOMOLO_ROBOT_ID}/planning_debug"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress  /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
upload_to_nas
;;
5*)
bag_gen_folder sensor_bag
docker exec -it qpilot bash -c "source /opt/qomolo/${ROS_WORKSPACE}/setup.bash &&  ros2 bag record /clock /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress  /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
upload_to_nas
;;
esac