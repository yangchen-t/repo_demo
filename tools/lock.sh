#!/bin/bash

source /opt/qomolo/utils/qpilot_setup/all_supervisord/.env || true

while :
do
	sleep 1
	key=`cat /home/nvidia/.env`
	if [[ $key == "xiangyang.chen" ]] || [[ $key == "ning.xu" ]] || [[ $key == "wenyou.chen" ]];then
		sudo chattr -R -i /opt/qomolo/qpilot-hw-param
		sudo chattr -R -i /opt/qomolo/qpilot-param
		sleep 300
		cd /opt/qomolo/qpilot-hw-param/ && git add . && git commit -m "$key" && sshpass -p xijingkeji git push
        sleep 100
	else
		echo "lock"
		chattr -R +i /opt/qomolo/qpilot-param
	       	chattr -R +i /opt/qomolo/qpilot-hw-param
	fi
	echo "" > /home/nvidia/.env
done
