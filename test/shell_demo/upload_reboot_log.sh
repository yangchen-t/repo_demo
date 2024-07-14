#!/bin/bash

readonly FILENAME="$(hostname).tar.gz"
readonly HOST_IP="192.168.103.172"
readonly HOSTS="westwell"
readonly PROBLEM=$1

function handle()
{
    find /var/log/ -maxdepth 1 -type f -exec sudo tar -zcvf /tmp/${FILENAME} {} +
}

function upload()
{
    ping ${HOST_IP} -c 2
    if [ $? -ne 0 ];then
        echo "scp failed, file is /tmp/"${FILENAME}; exit -1;
    else
        scp -P 2222 -o ServerAliveInterval=30 -o "StrictHostKeyChecking no" /tmp/${FILENAME} /tmp/readme-$(hostname).md ${HOSTS}@${HOST_IP}:~  
    fi
}

function get_basic_info()
{
    _sn=$(cat /sys/class/miivii/eeprom/hardware_sn)
    _device_info=$(cat /etc/miivii_release)
    echo {"time": ${PROBLEM}, "SN号": ${_sn}, "设备信息": ${_device_info}} | sudo tee /tmp/readme-$(hostname).md
}


get_basic_info && handle && upload

read -p "delete me? -> " y
if [[ ${y} == "y" ]];then
    sudo rm -r $0
fi