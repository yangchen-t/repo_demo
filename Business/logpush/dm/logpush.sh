#!/bin/bash

sudo chown -R $USER /data



function input_time_gen_folder(){
    mkdir -p /data/code/all_ws/ws/logpush_tmp
    read -p "请输入问题发生时的丹麦时间【examples:2022-04-21 15:00:00】:" PROBLEM_TIME
    if [[ ${#PROBLEM_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-02-22 12:00:00"
        exit 0
    else
        cd /data/code/all_ws/ws/logpush_tmp
        sudo rm -rf tmp
        TMP_LOG_NAME=${HOSTNAME}_`date +%Y-%m-%d-%H%M`_log_bag
        mkdir -p tmp/${TMP_LOG_NAME}/csv
        mkdir -p tmp/${TMP_LOG_NAME}/qlog
        mkdir -p tmp/${TMP_LOG_NAME}/supervisord_log
        mkdir -p tmp/${TMP_LOG_NAME}/localization_bag
        mkdir -p tmp/${TMP_LOG_NAME}/CO
        # mkdir -p tmp/${TMP_LOG_NAME}/lidar_bag
        # mkdir -p tmp/${TMP_LOG_NAME}/lidar_estop_bag
        input_timestamp=`date -d "$PROBLEM_TIME" +%s`
        # input_utc_timestamp=`expr $input_timestamp - 28800`
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

# 提供两种模式进行查询
# 按照时间进行搜索 + 按照文件进行搜索
# csv文件共有4种trajectory_conversion + igv_speed_lon_controller + igv_nlfb_lat_controller + alignment_log
function time_search_copy_csv(){
 #   if [[ ! -d " $DEPLOY_PATH_DEBUG" ]];then
 #       echo " $DEPLOY_PATH_DEBUG 路径不存在，请检查并创建"
 #       exit 0
 #   fi
    cd  $DEPLOY_PATH_DEBUG/csv
    search_time_stamp=`date -d "${PROBLEM_TIME}" +%s`
    older_time_stamp=`expr ${search_time_stamp} - 1800`
    OLDER_SEARCH_TIME=`date -d @$older_time_stamp +%Y-%m-%d\ %H:%M:00`
    newer_time_stamp=`expr ${search_time_stamp} + 1800`
    NEWER_SEARCH_TIME=`date -d @$newer_time_stamp +%Y-%m-%d\ %H:%M:00`
    find  $DEPLOY_PATH_DEBUG -name "trajectory*" -newermt "${OLDER_SEARCH_TIME}" ! -newermt "${NEWER_SEARCH_TIME}" | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv
}


function high_time_search_copy_csv(){
#    if [[ ! -d " $DEPLOY_PATH_DEBUG " ]];then
#        echo " $DEPLOY_PATH_DEBUG 路径不存在，请检查并创建"
#        exit 0
#    fi
    cd  $DEPLOY_PATH_DEBUG/csv
    search_time_stamp=`date -d "${SEARCH_TIME}" +%s`
    older_time_stamp=`expr ${search_time_stamp} - 86400`
    OLDER_SEARCH_TIME=`date -d @$older_time_stamp +%Y-%m-%d\ %H:%M:00`
    newer_time_stamp=`expr ${search_time_stamp} + 86400`
    NEWER_SEARCH_TIME=`date -d @$newer_time_stamp +%Y-%m-%d\ %H:%M:00`
    find ./ -name "$1*" -newermt "${OLDER_SEARCH_TIME}" ! -newermt "${NEWER_SEARCH_TIME}" | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv
}


# 低频csv文件，前后各两个
function file_search_copy_csv(){
    cd  $DEPLOY_PATH_DEBUG/csv
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 2 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv/
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 2 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv/
}

# 低频csv文件，前后各两个
function high_file_search_copy_csv(){
    cd  $DEPLOY_PATH_DEBUG/csv
    oldder_csv=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_csv} | head -n 20 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv/
    newer_csv=`find ./ -name "$1*" -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_csv} | head -n 20 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv/
}

# 上下一小时文件夹so提取
function Denmark_folder_search_co(){
    cd  $DEPLOY_PATH_DEBUG/csv/short_time
    mkdir -p  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/CO
    input_timestamp=`date -d "$PROBLEM_TIME" +%s`
    end_time=`expr $input_timestamp - 7200`
    START_TIME=`date -d @$end_time +%Y-%m-%d\ %H:%M:00`
    start_time=`expr $input_timestamp + 7200`
    END_TIME=`date -d @$start_time +%Y-%m-%d\ %H:%M:00`
    echo $START_TIME
    echo $END_TIME
    find  $DEPLOY_PATH_DEBUG/csv/short_time -name 'CO*' -type d -newermt "$START_TIME" ! -newermt "$END_TIME"  | xargs -I {} cp -r {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/CO
}

# keep error event
function keeper_error_event(){
    cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/keeper_error_event.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/
}

# log search pre
function log_search_copy_pre(){
    cd /data/code/all_ws/ws/
    beijing_date_mark=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    ls *.log | xargs -I  {} cp {}  /data/code/all_ws/ws/igv_log/{}-${beijing_date_mark}.log
}

# log search post
function log_search_copy_post(){
    cd /data/code/all_ws/ws/igv_log
    rm *$beijing_date_mark*
}

# 输入时间点前后各搜索四个文件日志模块
function file_search_copy_high_HZ_log(){
    beijing_date=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    cd /data/code/all_ws/ws/igv_log
    oldder_log=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -t ${oldder_log} | head -n 4 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
    newer_log=`find ./ -name "$1*"  -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -rt ${newer_log} | head -n 4 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
}

# 输入时间点前后各搜索两个文件日志模块
function file_search_copy_middle_HZ_log(){
    beijing_date=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    cd /data/code/all_ws/ws/igv_log
    oldder_log=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -t ${oldder_log} | head -n 2 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
    newer_log=`find ./ -name "$1*"  -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -rt ${newer_log} | head -n 2 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
}

# 输入时间点前后各搜索一个文件日志模块
function file_search_copy_low_HZ_log(){
    beijing_date=`date -d "8 hour" +%Y-%m-%d-%H-%M%S`
    cd /opt/qomolo/utils/ws_setup/cpc_supervisord/log
    oldder_log=`find ./ -name "$1*" ! -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -t ${oldder_log} | head -n 1 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
    newer_log=`find ./ -name "$1*"  -newermt "${SEARCH_TIME}" ! -path "./tmp/*" `
    ls -rt ${newer_log} | head -n 1 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
}

# 输入时间点前后15分钟内的二层数据
function search_copy_lidar_estop(){
    cd /data/code/all_ws/ws/lidar_estop_log
    start_input_timestamp=`date -d "$PROBLEM_TIME" +%s`
    start_utc_timestamp=`expr $start_input_timestamp - 29700`
    START_TIME=`date -d @$start_utc_timestamp +%Y-%m-%d\ %H:%M:00`
    end_input_timestamp=`date -d "$PROBLEM_TIME" +%s`
    end_utc_timestamp=`expr $end_input_timestamp  - 27900`
    END_TIME=`date -d @$end_utc_timestamp +%Y-%m-%d\ %H:%M:%S`
    find ./ -type d ! -path ./ -newermt "$START_TIME" ! -newermt "$END_TIME" | xargs -I {} cp -r {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/lidar_estop_bag/
}

# 输入时间点前后15分钟的定位数据包
function file_search_copy_odom(){
    cd /data/key_log/odom
    oldder_odom=`find ./ -name "*.db3" ! -newermt "${SEARCH_TIME}"`
    if [[ $oldder_odom != "" ]];then
        ls -t $oldder_odom | head -n 3 | xargs -I {} cp -r {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/localization_bag/
    fi
    newer_odom=`find ./ -name "*.db3" -newermt "${SEARCH_TIME}"`
    if [[ $newer_odom != "" ]];then
        ls -rt $newer_odom | head -n 3 | xargs -I {} cp -r {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/localization_bag/
    fi
}

# 嘉俊qp1069拷贝日志
function file_cp_for_jiajun(){
    read -p "输入开始时间：" INPUT_TIME
        if [[ ${#INPUT_TIME} != 19 ]];then
        echo "时间格式不对，无法执行，请按照格式来输入如2022-02-22 12:00:00"
        exit 0
    else
        cd /data/code/all_ws/ws/
        mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv
        cp local_plan.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cp mqtt_agent.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cp function_controller.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cp igv_agent.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cp qomolo_assembly.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cp vehicle_controller.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cd /data/code/all_ws/ws/logpush_tmp
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "local_plan*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "vehicle*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "mqtt*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "function_controller*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "igv_agent*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        find ./ -type f -newermt "${INPUT_TIME}" ! -path "./tmp/*" -name "qomolo_assembly*" | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
        cd /data/code/all_ws/ws/csv
        find ./ -type f -newermt "${INPUT_TIME}" ! -path ./ | xargs -I {} cp {}  /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/csv/
    fi
}

# 输入时间点搜索前30分钟+后30分钟的日志数据包
function time_search_log(){
    start_input_timestamp=`date -d "$PROBLEM_TIME" +%s`
    start_utc_timestamp=`expr $start_input_timestamp - 30600`
    START_TIME=`date -d @$start_utc_timestamp +%Y-%m-%d\ %H:%M:00`
    end_input_timestamp=`date -d "$PROBLEM_TIME" +%s`
    end_utc_timestamp=`expr $end_input_timestamp  - 27000`
    END_TIME=`date -d @$end_utc_timestamp +%Y-%m-%d\ %H:%M:%S`
    mkdir -p /data/code/all_ws/ws/logpush_tmp/${TMP_LOG_NAME}/qlog/$1
    cd /data/code/all_ws/ws/qlog/$1
    find ./ -type f ! -path ./ -newermt "$START_TIME" ! -newermt "$END_TIME" | xargs -I {} cp -r {} /data/code/all_ws/ws/logpush_tmp/${TMP_LOG_NAME}/qlog/$1/
}

# 输入时间点搜索前5个文件+后5个文件
function file_search_log(){
    cd  $DEPLOY_PATH_DEBUG/qlog/$1
    mkdir -p /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/qlog/$1/
    oldder_log=`find ./ -type f ! -newermt "${SEARCH_TIME}"`
    ls -t ${oldder_log} | head -n 20 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/qlog/$1/
    newer_log=`find ./  -type f   -newermt "${SEARCH_TIME}"`
    ls -rt ${newer_log} | head -n 20 | xargs -I {} cp {} /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/qlog/$1/
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
    sshpass -p xijingkeji scp  -o ServerAliveInterval=60  ${TMP_LOG_NAME}_$1.tar.gz qomolo@10.159.101.128:/key_log/key_log/
    if [ $? != 0 ];then
        echo -e "\033[031m数据因为网络原因传输失败，请联系管理员\033[0m"
        exit 0
    else
        echo "========================================数据传输到了地面站的如下路径==================================="
        echo /key_log/key_log/${TMP_LOG_NAME}_$1.tar.gz
        echo "=================================================================================================="
    fi
}


input_time_gen_folder
# trajectory csv
time_search_copy_csv
# common csv
file_search_copy_odom
file_search_copy_csv lattice_planner
high_time_search_copy_csv ws_lqr_lat_controller
high_time_search_copy_csv trajectory_conversion
file_search_copy_csv igv_speed_lon_controller
file_search_copy_csv lattice_planner
file_search_copy_csv planning_trajectorys
file_search_copy_csv planning_vehicle_state
file_search_copy_csv control 
file_search_copy_csv planning
Denmark_folder_search_co
# log pre
# log_search_copy_pre
# keep error event
# keeper_error_event
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/agent.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/assembly.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/canbus.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/container.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/control.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/empty_pc.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/function.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/keeper.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/keeper_error_event.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/lidar_driver.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/lidar_perception.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/localization_fuse.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/localization_adaptor.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/mqtt.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/navigation.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/safety_reporter.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/
cp /opt/qomolo/utils/ws_setup/cpc_supervisord/log/vdr.log /data/code/all_ws/ws/logpush_tmp/tmp/${TMP_LOG_NAME}/supervisord_log/

file_search_log agent
file_search_log container_operation_planner
file_search_log planning
file_search_log localization
file_search_log control
file_search_log keeper
# file_search_log alignment\ planner
# log post
# log_search_copy_post
upload_to_gcs log_bag
