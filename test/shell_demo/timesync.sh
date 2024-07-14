#!/bin/bash

nohup echo nvidia | sudo -S -i ntpdate -bs cn.ntp.org.cn 2>&1 &
_pid=$!

while true;
do
    sleep 1
    printf "\rCurrent time: %s" "${SECONDS}"
    if ! [[ $(ps -p ${_pid} | grep ${_pid}) ]];then
        echo "finish"
	    break
    fi
done

echo "time sync finish"
