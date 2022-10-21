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
上传定位坐船数据 6 ：
" MODE

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
    ls *.log.* | xargs -I  {} cp {}  /data/code/all_ws/ws/igv_log/{}-${beijing_date}.log
}


#keeper_error_event
function log_keeper_error_event_search_copy()
{
    cd /data/code/all_ws/ws/igv_log && rsync -azv --progress keeper_error_event.log ${workspace}/logpush_tmp/${UPLOAD_LOG_NAME}/
}
function log_history_search_copy()
{
    find /data/code/all_ws/ws/igv_log/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
    find /data/code/all_ws/ws/igv_log/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 3 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/supervisor_log
}
function csv_search_copy()
{
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 2 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
}
function high_csv_search_copy()
{
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/csv
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
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/short_time/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 1 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
    find /data/code/all_ws/ws/${CSV_FOLDER_NAME}/short_time/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 1 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/vdr
}
function folder_search_lidar()
{
    cd /data/key_log/lidar
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

function localization_bag(){
        UPLOAD_LOG_NAME=${HOSTNAME}_`date -d "8 hour" +%Y-%m-%d-%H%M`_localization_collect
        mkdir -p /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/odom_bag
        if [[ ${#START_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-02-22 12:00:00"
        exit 0
        fi
        if [[ ${#END_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-02-22 12:00:00"
        exit 0
        fi
        cd ${ODOM_FOLDER_NAME}
        nice -n 19 find ./ -name '*.db3' -type f -newermt "$START_TIME" ! -newermt "$END_TIME"  | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/odom_bag/
}
function localization_log(){      
        UPLOAD_LOG_NAME=${HOSTNAME}_`date -d "8 hour" +%Y-%m-%d-%H%M`_localization_collect
        mkdir -p /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_check_log 
        mkdir -p /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/keep_log
        cd /data/code/all_ws/ws/igv_log
        start_time=`date -d "$START_TIME" +%s`
        start_utc=`expr $start_time - 28000`
        start_bj=`date -d @$start_utc "+%Y-%m-%d %H:%M:%S"`
        end_time=`date -d "$END_TIME" +%s`
        end_utc=`expr $end_time - 28000`
        end_bj=`date -d @$end_utc "+%Y-%m-%d %H:%M:%S"`
        nice -n 19 find ./ -name 'localization_check*' -type f -newermt "$start_bj" ! -newermt "$end_bj"  | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/localization_check_log/  
        nice -n 19 find /data/code/all_ws/ws/igv_log -name "keep*" -type f -newermt "$start_bj" ! -newermt "$end_bj"  | xargs -I {} rsync -avz --progress  {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/keep_log/  
}
###############################################################
function folder_search_image_xm(){
    
    find /data/code/all_ws/ws/key_log/image/$1* -type d ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
    find /data/code/all_ws/ws/key_log/image/$1* -type d  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/images
}
function folder_search_lidar_xm(){

    find /data/code/all_ws/ws/key_log/lidar/* -type d ! -newermt "${SEARCH_TIME}" | tail -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
    find /data/code/all_ws/ws/key_log/lidar/* -type d  -newermt "${SEARCH_TIME}" | head -n 5 | xargs -I {} rsync -avz --progress {} /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/lidar
}

function upload_to_nas()
{
    rsync -avz --progress   /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
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
    rsync -avz --progress /opt/qomolo/qpilot/qpilot.repos /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
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
        echo "========================================请把以下路径粘贴到issue==================================="
        echo ${UPLOAD_PATH}/${UPLOAD_LOG_NAME}.tar.gz
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
    log_history_search_copy function_control
    log_history_search_copy mqtt_adaptor
    log_history_search_copy mono_lane_tracker_ros2
    log_history_search_copy canbus
    log_history_search_copy local_plan
    log_history_search_copy localization_checker
    log_history_search_copy vehicle_control
    log_history_search_copy qomolo_assembly
    log_history_search_copy alignment_planner
    log_history_search_copy agent
    log_history_search_copy keeper 
    log_history_search_copy landmark_localizer
    log_history_search_copy lidar_estop
    log_history_search_copy lidar_preprocess
    log_history_search_copy localization_logger
    log_history_search_copy vehicle_data_recorder
    log_history_search_copy wheel_odom
    log_history_search_copy localization_adaptor 
    log_history_search_copy gnss_driver
    log_history_search_copy gnss_processor
    log_history_search_copy hesai_lidar_4in1 
    log_history_search_copy ros2_http
    log_history_search_copy http_bridge
    log_history_search_copy lidar_config_check 
    log_history_search_copy fusion
    log_history_search_copy mono_lane_tracker
    log_history_search_copy lidar_cps_alignment
    log_history_search_copy lstr
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
    #images
    if [[ "${HOSTNAME}" =~ ^hr.*105 ]];then
        echo "105"
        folder_search_image_xm 2022
    elif [[ "${HOSTNAME}" =~ ^hr.*106 ]];then
        echo "106"
        folder_search_lidar_xm
    else
        echo "other"
        folder_search_image 2022
        folder_search_lidar
    fi
}
#upload
case "$MODE" in
1*)
#天津
if [[ "${HOSTNAME}" =~ ^TJ_IGV.* ]] || [[ "${HOSTNAME}" =~ ^CEKE_IGV.* ]] || [[ "${HOSTNAME}" =~ ^CN_CK.* ]] || [[ "${HOSTNAME}" =~ ^hr.* ]] || [[ "${HOSTNAME}" =~ ^pd.* ]];then
    main
    upload_to_gcs
elif [[ "${HOSTNAME}" =~ ^wh.* ]] || [[ "${HOSTNAME}" =~ ^dl.* ]];then
    main
    upload_to_nas
else 
    echo "所在项目不支持"
fi
;;
# 录定位数据包
2*)
bag_gen_folder localization_bag
docker exec -it ppc_igv bash -c "source /opt/qomolo/qpilot/setup.bash &&  ros2 bag record /clock /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom /${QOMOLO_ROBOT_ID}/localization/odom /${QOMOLO_ROBOT_ID}/full_pointcloud"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress  /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
if [[ "${HOSTNAME}" =~ ^wh.* ]] || [[ "${HOSTNAME}" =~ ^dl.* ]];then
      upload_to_nas
else 
      upload_to_gcs
fi
;;
# 录感知数据包
3*)
bag_gen_folder perception_bag
docker exec -it ppc_igv bash -c "source /opt/qomolo/qpilot/setup.bash && ros2 bag record /${QOMOLO_ROBOT_ID}/tf /${QOMOLO_ROBOT_ID}/tf_static /${QOMOLO_ROBOT_ID}/lidar_estop_viz /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom /${QOMOLO_ROBOT_ID}/pandar/front_left /${QOMOLO_ROBOT_ID}/pandar/front_right /${QOMOLO_ROBOT_ID}/pandar/rear_left /${QOMOLO_ROBOT_ID}/pandar/rear_right /rslidar_points/front /rslidar_points/rear /${QOMOLO_ROBOT_ID}/lidar_preprocess/wheelbox /${QOMOLO_ROBOT_ID}/filtered_pointcloud"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
if [[ "${HOSTNAME}" =~ ^wh.* ]] || [[ "${HOSTNAME}" =~ ^dl.* ]];then
      upload_to_nas
else 
      upload_to_gcs
fi
;;
# 录规划数据包
4*)
bag_gen_folder collision_bag
docker exec -it ppc_igv bash -c "source /opt/qomolo/qpilot/setup.bash &&  ros2 bag record /${QOMOLO_ROBOT_ID}/tf /${QOMOLO_ROBOT_ID}/tf_static /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/localization/odom /${QOMOLO_ROBOT_ID}/filtered_pointcloud /${QOMOLO_ROBOT_ID}/local_plan_new /${QOMOLO_ROBOT_ID}/planning_debug"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
if [[ "${HOSTNAME}" =~ ^wh.* ]] || [[ "${HOSTNAME}" =~ ^dl.* ]];then
      upload_to_nas
else 
      upload_to_gcs
fi
;;
5*)
bag_gen_folder sensor_bag
docker exec -it ppc_igv bash -c "source /opt/qomolo/qpilot/setup.bash &&  ros2 bag record /clock /${QOMOLO_ROBOT_ID}/odom /${QOMOLO_ROBOT_ID}/gnss/odom"
bag_folder=`ls rosbag2* -d -t | head -n 1`
echo "已经录制成功的数据是这份： /data/code/all_ws/ws/"$bag_folder
rsync -avz --progress --bwlimit=1000      -r /data/code/all_ws/ws/$bag_folder /data/code/all_ws/ws/logpush_tmp/${UPLOAD_LOG_NAME}/
if [[ "${HOSTNAME}" =~ ^wh.* ]] || [[ "${HOSTNAME}" =~ ^dl.* ]];then
      upload_to_nas
else 
      upload_to_gcs
fi
;;
6*)
read -p "输入坐船开始时间：" START_TIME
read -p "输入坐船结束时间：" END_TIME
read -p "是否需要rosbag y/n : " number
if [[ "$number" = "y" ]] || [[ "$number" = "Y" ]] || [[ "$number" = "" ]] || [[ "$number" = "yes" ]];then
    localization_bag
    keeper_error_event
    localization_log 
    upload_to_gcs
else 
    localization_log
    keeper_error_event
    upload_to_gcs
fi
esac