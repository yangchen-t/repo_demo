#!/bin/bash

set -e 

# arch 
# if [[ `arch` =~ "x86" ]];then
#     echo "x86"
# elif [[ `arch` =~ "aarch64" ]];then
#     echo "arm"
# fi

sudo apt update  -y


echo -e "\033[31m the new ws packages (top10) \033[0m"
sudo apt-cache madison ws-cpc  | head -n 10 | awk '{print$1 , $3}'
echo -e "\033[31m==================================================\033[0m"
echo -e "\033[31m old ws packages (top10) \033[0m"
sudo apt-cache madison ws-cpc-ng | head -n 10 | awk '{print$1 , $3}'
echo -e "\033[31m==================================================\033[0m"
echo -e "\033[31m PTI \033[0m"
sudo apt-cache madison ws-onsite-ws-cpc-ng | head -n 10 | awk '{print$1 , $3}'
echo -e "\033[31m==================================================\033[0m"

echo -e "\033[31m Current Version \033[0m"
dpkg -l | grep ws-cpc | grep "ii"
echo -e "\033[31m==================================================\033[0m"
read -p "please input update version : 
template: ws-cpc=0.4xxxxxxx :  " VERSION

if [[ ${VERSION} == "" ]];then
    echo "input is empty!"
    exit 0
fi

packages_real=`echo ${VERSION} | awk -F "=" '{print$1}'`
packages_list="ws-cpcws-cpc-ngws-onsite-ws-cpc-ng"
if [[ ${packages_list} =~ ${packages_real} ]];then
    let NOW_VERSION=`dpkg -l | grep ws-cpc | grep "ii" | awk '{print$2}'`
    if [[ ${packages_real} != ${NOW_VERSION} ]];then
        sudo apt remove $NOW_VERSION -y; sudo apt install --allow-downgrades  ${VERSION} -y
    fi
    sudo apt install --allow-downgrades  ${VERSION} -y
else
    echo "packages name error, please check"
fi

echo "================================================="
if [[ `arch` =~ "x86" ]];then
    echo "x86"
elif [[ `arch` =~ "aarch64" ]];then
    read -p "是否重启docker <y or n>" reboot
    if [[ $reboot == "y" ]];then
	    cd /opt/qomolo/utils/qpilot_setup/ws_supervisord/ && bash start_container.sh
    elif [[ $reboot == "n" ]];then
	    echo "你没有选择重启"
    else
	    exit 0 
    fi 
fi



