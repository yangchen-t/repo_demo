#!/bin/bash



read -p "是否需要rosbag y/n : " number
if [[ "$number" = "y" ]] || [[ "$number" = "Y" ]] || [[ "$number" = "" ]];then
#    localization_bag
#    localization_log
#    upload_to_gcs
    	echo "ok"
else 
	echo "else"
fi 

