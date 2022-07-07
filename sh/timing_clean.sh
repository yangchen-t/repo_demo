#!/bin/bash
#"""
#为每个xavier 定期清理空间释放。
#""" 


sudo  chown -R nvidia /data/code/all_ws/ws
function clean_lidar_estop_log()
{
    cd /data/code/all_ws/ws/lidar_estop_log/
    time=`date`
    current_time=`date -d "$time" +%s`
    utc_time=`expr $current_time - 7776000`
    bj_time=`date -d @$utc_time +%Y%m%d\ %H:%M:00`
    new_time=${bj_time:0:6}
    ls | grep "$new_time" | xargs -I {}  rm -rvf {}     #debug  == rm -rvf 
}

function clean_debug()
{
    cd /data/code/all_ws/ws
    ls | grep -E "^rosbag|^localization" | xargs -I {} rm -rf {}   
}

disk_len=`df -h | grep /data| grep -v docker | awk '{print $4}'  | cut -f 1 -d "G"`
while true 
do
        sleep 60
        if [ "$disk_len" -lt "100" ];then
            clean_lidar_estop_log
            clean_debug
        else
            echo "ok"
            echo $disk_len
        fi
done

