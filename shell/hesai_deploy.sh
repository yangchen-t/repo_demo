#!/bin/bash 

echo "---> start lidar config <---"
lidar_key_list='11 12 13 14'
for i in $lidar_key_list
do
	cd /opt/qomolo/utils/lidar_config/hesai_config/ && python3 setup_config.py 192.168.10.$i $i
done