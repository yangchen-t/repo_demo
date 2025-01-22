#!/bin/bash

host=nvidia
ip=192.168.103.42

sshpass -p ${host} ssh ${host}@${ip} "rm -r /tmp/debs; mkdir -p /tmp/debs ; echo ${host} | sudo -S apt update"
 
download_re()
{   local deb=${1}
    sshpass -p ${host} ssh ${host}@${ip} "cd /tmp/debs && apt download ${deb} -y"
}

for i in $(cat ./config.txt);do
    download_re ${i}
done

echo "scp -r ${host}@${ip}:/tmp/debs/ ./offline_debs"