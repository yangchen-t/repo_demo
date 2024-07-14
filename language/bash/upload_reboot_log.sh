#!/bin/bash

readonly FILENAME="$(hostname).tar.gz"
readonly HOST_IP="192.168.103.172"
readonly HOSTS="westwell"
readonly PASSWD=" "

function handle()
{
    find /var/log/ -maxdepth 1 -type f -exec sudo tar -zcvf /tmp/${FILENAME} {} +
}

function upload()
{
    ping ${HOST_IP} -c 1
    if [ $? -ne 0 ];then
        echo "scp failed, file is /tmp/"${FILENAME}
        exit -1;
    else
        sshpass -p ${PASSWD} scp -o ServerAliveInterval=30 -o "StrictHostKeyChecking no" /tmp/${FILENAME} ${HOSTS}@${HOST_IP}:~  
}


handle && upload