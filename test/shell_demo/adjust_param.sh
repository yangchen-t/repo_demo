#!/bin/bash

set -u 

perception_path="/opt/qomolo/qpilot/temp/parameter/profile/driver/ica/startup.yaml"
agent_path="/opt/qomolo/qpilot-orin/share/qpilot_parameters/agent/ica/agent_ica.yaml"

OPTIONS=${1:-"adjust"}
declare -g g_reset_flag=

usage()
{
    echo "OPTIONS $0 "
    echo -e "\tbash $0       : defualt adjust param"
    echo -e "\tbash $0 check : check param"
    echo -e "\tbash $0 reset : reset param"
}

perception_config()
{        
    sudo sed -i 's/106: \["lidar_preprocess","top_obj_det"\]/106: \["lidar_preprocess"\]/g' ${perception_path}
    if [[ ${g_reset_flag} ]];then
        sudo sed -i 's/106: \["lidar_preprocess"\]/106: \["lidar_preprocess","top_obj_det"\]/g' ${perception_path}
    fi 
}

agent_config()
{

    sudo sed -i 's/check_obs_height_mode: 1/check_obs_height_mode: 0/g' ${agent_path}
    if [[ ${g_reset_flag} ]];then
        sudo sed -i 's/check_obs_height_mode: 0/check_obs_height_mode: 1/g' ${agent_path}
    fi 
}

all()
{
    perception_config
    agent_config   
}

check()
{
    echo "=========== agent param result ==========="
    cat ${agent_path} | grep "check_obs_height_mode"
    echo "=========== perception param result ==========="
    cat ${perception_path} | grep "startup" -A 2

}
case ${OPTIONS} in 
"reset") 
    g_reset_flag=${OPTIONS}
    all ;;
"check")
    check ;;
"-h")
    usage ;;
*) 
    all ;;
esac