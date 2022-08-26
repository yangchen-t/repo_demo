#!/bin/bash

if [[ $1 == '' ]] && [[ $2 == '' ]] && [[ $3 == '' ]] && [[ $4 == '' ]];then
      echo "示例 ：
      bash autodeploy.sh 10.159.2.106 dl2-param 0.6.3.46-81503focal.20220824.185443 0.2.81-81508focal.20220824.184413
      "
      exit
fi

if [[ $1 == '' ]] ;then 
      echo "缺少 qomolo_ip"
      exit
fi
if [[ $2 == '' ]] ;then 
      echo "缺少 hostname"
      exit
fi
if [[ $1 == '' ]] ;then 
      echo "缺少 qpilot版本号"
      exit
fi
if [[ $1 == '' ]] ;then 
      echo "缺少 qpilot-param版本号"
      exit 
fi

QOMOLO_IP=$1
QOMOLO_ROBOT_ID=$2
qpilot=$3
qpilot-param=$4

sudo chown -R nvidia /etc/hostname
echo nvidia | sudo -S echo "$QOMOLO_ROBOT_ID" > /etc/hostname     

FIND_FILE="/etc/ssh/ssh_config"
FIND_STR="StrictHostKeyChecking no"
# 判断匹配函数，匹配函数不为0，则包含给定字符
if [ `grep -c "$FIND_STR" $FIND_FILE` -ne '0' ];then
    echo "ok"
else 
    sudo chown -R nvidia /etc/ssh/ssh_config
    echo nvidia | sudo -S echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
fi 

sudo apt update
echo "---> clean netplan config <---"
sudo mv /etc/netplan/* ~/

echo nvidia | sudo -S touch /etc/netplan/50-bond.yaml
sudo chown -R nvidia /etc/netplan

echo "---> set netplan config <---"
sudo echo "
network:
    version: 2
    renderer: networkd
    ethernets:
      eth0:
        dhcp4: yes
        optional: true
      eth1:
        optional: true
      eth2:
        optional: true
      eth3:
        dhcp4: yes
        optional: true
    bonds:
        bond0:
            addresses: [$QOMOLO_IP/24]
            gateway4: ${QOMOLO_IP:0:8}.1
            nameservers:
               addresses: [${QOMOLO_IP:0:8}.1]
            dhcp4: false
            interfaces:
                - eth1
                - eth2
            parameters:
                mode: 802.3ad
                transmit-hash-policy: layer3
                mii-monitor-interval: 100
                learn-packet-interval: 100
    vlans:
        bond0.sen:
            id: 2
            link: bond0
            addresses: [192.168.10.${QOMOLO_IP:9}/24]
" > /etc/netplan/50-bond.yaml

echo "---> install <---"
sudo apt install qomolo-miivii-l4t-core qomolo-miivii-l4t-modules  qomolo-mcbind qomolo-ptp qomolo-sys-monitor
sudo apt install qomolo-lidar-config sshpass vim  qpilot-setup qomolo-gcs-scripts 

echo "---> deploy lidar launch <--- "

cd /opt/qomolo/utils/qpilot_setup/tools/ && bash lidar_deploy.sh new-version.tar.gz    #new-veriosn.tar.gz  为最新版本激光驱动  (也可以注释掉这一步进行手动执行) 
echo "暂时不更新可以回车跳过！！"
read -p "input qpilot version :" qpilot
read -p "input qpilot-param version :" qpilot_param
if [[ $qpilot != "" && $qpilot_param != "" ]];then
	sudo apt update; sudo apt install qpilot=$qpilot
	sudo apt update; sudo apt install qpilot-param=$qpilot_param
else
	echo "---> skip next <---"
fi

echo "---> start lidar config <---"

lidar_key_list='11 12 13 14'
for i in $lidar_key_list
do
	cd /opt/qomolo/utils/lidar_config/hesai_config/ && python3 setup_config.py 192.168.10.$i $i
done
echo "---> finish <---"

sudo netplan apply
sudo reboot
