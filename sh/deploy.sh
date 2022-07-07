#!/bin/bash

sudo apt update;sudo apt install igv-sensor 

if [ -f /home/$USER/Downloads/lidarview ];then
	sudo cp /home/$USER/Downloads/lidarview /bin/lidarview
	sudo chmod a+x /bin/lidarview 
	echo "部署完成---> 可以使用lidarview进行定位反投影操作"
elif [ -f /home/$USER/下载/lidarview ];then
        sudo cp /home/$USER/下载/lidarview /bin/lidarview
        sudo chmod a+x /bin/lidarview
	echo "部署完成---> 可以使用lidarview进行定位反投影操作"
else
	echo "请确定Downloads/下载 路径下存在lidarview该文件"

fi
