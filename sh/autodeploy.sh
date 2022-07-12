#!/bin/bash


sudo apt update
echo "clean netplan config "
sudo mv ~/etc/netplan/* ~/

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
sudo apt install qomolo-miivii-l4t-core qomolo-miivii-l4t-modules  qomolo-mcbind
sudo apt install qomolo-mcbind  qomolo-lidar-config sshpass vim 

echo "deploy lidar launch "
if [[ ! -d /opt/qomolo/gst-plugin/plugin ]];then
	sudo mkdir -p /opt/qomolo/gst-plugin/plugin 
	sudo sshpass -p xijingkeji scp -o "StrictHostKeyChecking no" user@10.159.101.1:~/0618.tar.gz .
      	sudo tar -xvf 0618.tar.gz -C /opt/qomolo/gst-plugin/plugin
else
	sudo sshpass -p xijingkeji scp -o "StrictHostKeyChecking no" user@10.159.101.1:~/0618.tar.gz .
        sudo tar -xvf 0618.tar.gz -C /opt/qomolo/gst-plugin/plugin
fi

echo "暂时不更新可以回车跳过！！"
read -p "input qpilot version :" qpilot
read -p "input qpilot-param version :" qpilot_param
read -p "input qpilot-setup version :" qpilot_setup
if [[ $qpilot != "" && $qpilot_param != "" && $qpilot_setup != "" ]];then
	sudo apt update; sudo apt install qpilot=$qpilot
	sudo apt update; sudo apt install qpilot-param=$qpilot_param
	sudo apt update; sudo apt install qpilot-setup=$qpilot_setup
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

	
