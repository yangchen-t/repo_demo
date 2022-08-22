#!/bin/bash

QOMOLO_ROBOT_ID=$2

echo nvidia | sudo -S echo '`$2`' > /etc/hostname 
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
echo "clean netplan config "
sudo mv ~/etc/netplan/* ~/

sudo chown -R nvidia /etc/netplan
echo nvidia | sudo -S touch /etc/netplan/50-bond.yaml
echo "set netplan config"
echo "
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
            addresses: [10.159.$1.105/24]
            gateway4: 10.159.$1.1
            nameservers:
               addresses: [10.159.$1.1]
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
            addresses: [192.168.10.105/24]
" > ~/etc/netplan/50-bond.yaml

echo "install"
sudo apt install qomolo-miivii-l4t-core qomolo-miivii-l4t-modules  qomolo-mcbind qomolo-ptp qomolo-sys-monitor
sudo apt install qomolo-lidar-config sshpass vim  qpilot-setup qomolo-gcs-scripts

echo "deploy lidar launch "
if [[ ! -d /opt/qomolo/gst-plugin/plugins ]];then
	sudo mkdir -p /opt/qomolo/gst-plugin/plugins 
	sudo sshpass -p xijingkeji scp -o "StrictHostKeyChecking no" user@10.159.201.1:~/0618.tar.gz .
      	sudo tar -xvf 0618.tar.gz -C /opt/qomolo/gst-plugins/plugin
else
	sudo sshpass -p xijingkeji scp -o "StrictHostKeyChecking no" user@10.159.201.1:~/0618.tar.gz .
        sudo tar -xvf 0618.tar.gz -C /opt/qomolo/gst-plugins/plugin
fi

echo "暂时不更新可以回车跳过！！"
read -p "input qpilot version :" qpilot
read -p "input qpilot-param version :" qpilot_param
if [[ $qpilot != "" && $qpilot_param != "" ]];then
	sudo apt update; sudo apt install qpilot=$qpilot
	sudo apt update; sudo apt install qpilot-param=$qpilot_param
else
	echo "skip next"
fi

echo "start lidar deploy"

python3 /opt/qomolo/utils/lidar_config/hesai_config/setup_config.py 192.168.10.11 11
python3 /opt/qomolo/utils/lidar_config/hesai_config/setup_config.py 192.168.10.12 12
python3 /opt/qomolo/utils/lidar_config/hesai_config/setup_config.py 192.168.10.13 13
python3 /opt/qomolo/utils/lidar_config/hesai_config/setup_config.py 192.168.10.14 14

echo "finish"

sudo netplan apply

	
