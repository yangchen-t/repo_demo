#!/bin/bash


if [ -f /home/$USER/Downloads/start_rviz2.zip ];then
	sudo cp /home/$USER/Downloads/start_rviz2.zip ~/qpilot_dev_ws
	cd ~/qpilot_dev_ws && sudo unzip start_rviz2.zip && sudo chmod +x start_rviz.sh play.sh  
	echo "部署完成---> 可以使用start_rviz2.sh进行二层可视化操作
		--------->  docker 内使用！！！！<------------
	      先使用play.sh + rosbag    --->播放数据包，默认不加 -l 
	      再使用start_rviz2.sh      --->二层可视化
	"
elif [ -f /home/$USER/下载/start_rviz2.zip ];then
        sudo cp /home/$USER/下载/start_rviz2.zip  ~/qpilot_dev_ws
        cd ~/qpilot_dev_ws && sudo unzip start_rviz2.zip && sudo chmod +x start_rviz.sh play.sh
	echo "部署完成---> 可以使用start_rviz2.sh进行二层可视化操作
	        --------->  docker 内使用！！！！<------------
              先使用play.sh + rosbag    --->播放数据包，默认不加 -l 
              再使用start_rviz2.sh      --->二层可视化
	"
else
	echo "请确定Downloads/下载 路径下存在start_rviz2.zip该文件"
fi
