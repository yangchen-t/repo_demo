#!/bin/bash

sudo chown -R $USER /data



function input_time_gen_folder(){
    mkdir -p /data/code/all_ws/ws/logpush_tmp
    read -p "请输入问题发生时的瑞典时间【examples:2022-04-21 15:00:00】:" PROBLEM_TIME
    if [[ ${#PROBLEM_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-02-22 12:00:00"
        exit 0
    else
        cd /data/code/all_ws/ws/logpush_tmp
        TMP_LOG_NAME=${HOSTNAME}_`date +%Y-%m-%d-%H%M`_log_bag
        mkdir -p tmp/${TMP_LOG_NAME}/csv
        mkdir -p tmp/${TMP_LOG_NAME}/supervisord_log
        input_timestamp=`date -d "$PROBLEM_TIME" +%s`
        SEARCH_TIME=`date -d @$input_timestamp +%Y-%m-%d\ %H:%M:00`
    fi
}

function bag_gen_folder(){
    cd /data/code/all_ws/ws/logpush_tmp
    sudo rm -rf tmp
    TMP_LOG_NAME=${HOSTNAME}_`date -d "8 hour" +%Y-%m-%d-%H%M`_$1
    mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}
    cd /data/code/all_ws/ws
}

function time_search_copy_csv(){
#    search_time_stamp=`date -d "${PROBLEM_TIME}" +%s`
#    older_time_stamp=`expr ${search_time_stamp} - 1800`
#    OLDER_SEARCH_TIME=`date -d @$older_time_stamp +%Y-%m-%d\ %H:%M:00`
#    newer_time_stamp=`expr ${search_time_stamp} + 1800`
#    NEWER_SEARCH_TIME=`date -d @$newer_time_stamp +%Y-%m-%d\ %H:%M:00`
    find /home/$USER/ws_ppc_ws/$1* -type f ! -newermt "${SEARCH_TIME}" | grep $1 | tail -n 5 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv
    find /home/$USER/ws_cpc_ws/$1* -type f  -newermt "${SEARCH_TIME}" | grep $1 | head -n 5 | xargs -I {} cp  {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv
}



function upload_to_gcs(){
    echo "=========================================以下数据正在被压缩========================================="
    cp /opt/qomolo/ws_cpc_ng/ws_cpc_ng.repos /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/
    cd /data/code/all_ws/ws/logpush_tmp/tmp/
    sudo tar -zcvf ${TMP_LOG_NAME}_$1.tar.gz ${TMP_LOG_NAME}
    YEAR=`date -d "8 hour" +%Y`
    MONTH=`date -d "8 hour" +%-m`
    DAY=`date -d "8 hour" +%-d`
    UPLOAD_PATH=${NAS_PATH}/${YEAR}/${MONTH}/${DAY}/${HOSTNAME}
    echo "===========================================数据压缩已完成=========================================="
    echo "数据正在传输中......"
    sshpass -p q scp  -o ServerAliveInterval=60  ${TMP_LOG_NAME}_$1.tar.gz qomolo@10.159.101.128:/key_log/key_log/
    if [ $? != 0 ];then
        echo -e "\033[031m数据因为网络原因传输失败，请联系管理员\033[0m"
        exit 0
    else
        echo "========================================数据传输到了地面站的如下路径==================================="
        echo /key_log/key_log/${TMP_LOG_NAME}$1.tar.gz
        echo "=================================================================================================="
    fi
}


input_time_gen_folder
cp /opt/qomolo/utils/ws_setup/navi_supervisord/log/navigation.log  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log
cp /opt/qomolo/utils/ws_setup/navi_supervisord/log/lidar_driver.log  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log
cp /opt/qomolo/utils/ws_setup/navi_supervisord/log/lidar_perception.log  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log

time_search_copy_csv first_level_safety
time_search_copy_csv lattice_planner
time_search_copy_csv planning_vehicle
time_search_copy_csv prediction_data
time_search_copy_csv control 
time_search_copy_csv planning
time_search_copy_csv trajectory_conversion

upload_to_gcs log_bag
bag_gen_folder
