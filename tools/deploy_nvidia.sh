#!/bin/bash

igv_passwd xiangyang.chen
sleep 1
cd /opt/qomolo/ && rm -rf qpilot-hw-param
systemctl stop qomolo-hw-param.service 
cd /lib/systemd/system/ && sudo rm qomolo-hw-param.service

sudo chown -R nvidia /opt
sudo apt update
#sudo apt install python3-watchdog

source /opt/qomolo/utils/qpilot_setup/all_supervisord/.env || true

QOMOLO_ROBOT_ID=`echo $QOMOLO_ROBOT_ID`

cd /opt/qomolo/ && sshpass -p xijingkeji git clone ssh://user@10.159.$1.1:22/data/qpilot-hw-param/.git  && \
cd /opt/qomolo/qpilot-hw-param && git checkout ${QOMOLO_ROBOT_ID}-param &&

sshpass -p xijingkeji git pull origin ${QOMOLO_ROBOT_ID}-param &&  \

echo "[user]
    name = xiangyang.chen
    email = xiangyang.chen@westwell-lab.com
"  >> /opt/qomolo/qpilot-hw-param/.git/config


#install  lock.service
sudo cp /opt/qomolo/utils/qpilot_setup/tools/qomolo-hw-param.service /lib/systemd/system/
systemctl enable qomolo-hw-param.service
systemctl start qomolo-hw-param.service
systemctl restart qomolo-hw-param.service
