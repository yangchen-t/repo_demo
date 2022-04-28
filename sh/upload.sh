#!/bin/bash

#read -p "Enter the vehicle number ~:" vehicle
current_time="`date +%Y-%m-%d-%H-%M-%S`"
time_now="`date +%Y-%m-%d' '%H:%M:%S`"
start_time="`date -d "-3 hour" +%F' '%H:%M:%S`"

echo $current_time
filename=ceke$1_$current_time

files=`find ./ -name '*' -newermt "$start_time" ! -newermt "$time_now"`
cmd=`mkdir log && cp -r $files log/ && zip -r ceke$1_$current_time.zip log/ && rm -rf log/`

echo "start compress"
docker exec -it ceke$1 bash -c "cd tmp/ && $cmd  " 1>/dev/null 2>/dev/null
docker cp ceke$1:/tmp/ceke$1_$current_time.zip . &&


sshpass -p AAxijing123.. sftp xiangyang.chen@192.168.103.77: <<EOF
put /home/qomolo/ceke$1_$current_time.zip /data/cn_ceke_data/
EOF

clear
echo "Upload complete!"
echo "NAS path!"
echo "/data/cn_ceke_data/ceke$1_$current_time.zip"  

