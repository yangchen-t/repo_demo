#!/bin/bash

# 增加包版本校验

declare -A  CanConfigMap=(
    ["can0"]="500000"
    ["can1"]="500000"
    ["can2"]="250000"
    ["can3"]="250000"
)
declare -A VechcleMap=(
    ["igv"]="igv"
    ["qt"]="qtruck"
    ["qthd"]="qtruck"
    ["ws"]="asc"
    ["qbus"]="bus"
    ["bus"]="bus"
    ["et"]="etruck"
    ["tug"]="qtractor"
)

opts=${1}
config="./config.txt"

declare -g NetStats=${opts:-"online"}

GLOBAL_PROFILE="/etc/qomolo/profile/global/profile.yaml"
PROJECT_PROFILE="/etc/qomolo/profile/project/profile.yaml"
VEHICLE_PROFILE="/etc/qomolo/profile/vehicle_type/profile.yaml"

PROJECT_NAME=$(yq ".profile_name" ${PROJECT_PROFILE})
QOMOLO_ROBOT_ID=${PROJECT_NAME}$(yq ".vehicle_id" ${GLOBAL_PROFILE})

vt=$(yq ".profile_name" ${VEHICLE_PROFILE})
case ${vt} in
    igv*|bus*|tug*) vehicle_type=${vt:0:3};;
    qthd*|qbus*) vehicle_type=${vt:0:4} ;;
    qt*|ws*|et*) vehicle_type=${vt:0:2} ;;
    *) vehicle_type="igv" ;;
esac

USAGE()
{
    echo "Usage:bash $(basename $0) [option]"
    echo "Options:"
    echo -e "\t online                   :Online quick deploy."
    echo -e "\t offline                  :Offline quick deploy."
    echo -e "\t check                    :Check deploy result."
}

INSTALL_DEBS()
{
    case ${NetStats} in
    "online") sudo apt update  
        for i in $(cat ${config});do
            sudo apt install ${i} -y 
        done ;;
    "offline")
        sudo apt install ./debs/* ;;
    esac
}

CAN_CONFIG_CHECK()
{
    local config="/etc/network/interfaces"
    for key in "${!CanConfigMap[@]}"; do
        if [[ $(cat ${config} | grep "${key}" | grep bitrate | awk '{print$9}') != ${CanConfigMap["${key}"]} ]];then
            tLogger "${key} check failed" E 
        fi
    done
}

LOGPUSH_CONFIG()
{
    local logpush_env="/opt/qomolo/utils/qomolo_gcs_scripts/log/.env"
    local logpush_config_status=$(cat ./.logpush_status 2>/dev/null || echo "false")

    QOMOLO_ROBOT_ID=$(yq ".profile_name" ${PROJECT_PROFILE})$(yq ".vehicle_id" ${GLOBAL_PROFILE})
    NAS_PATH="/data/qpilot_log/"${vehicle_type}
    
    if [[ ${logpush_config_status} == "true" ]];then
        read -p  "maybe your deploy logpush config already?, cover? <y/n>" ipt
        case ${ipt} in 
        "y"|""|"Y") logpush_config_status="false" ;;
        *)  tLogger "skip deploy logpush config!" W ; return 0;;
        esac
    fi 
    if [[ ${logpush_config_status} == "false" ]];then
        case ${NetStats} in
        "offline")
            read -p "gcs username: " GCS_USERNAME
            read -p "gcs ip: " GCS_IP
            read -p "gcs passwd: " GCS_PASSWORD
        ;;
        esac
        echo "
export QOMOLO_ROBOT_ID=${QOMOLO_ROBOT_ID}
export GCS_PASSWORD=${GCS_PASSWORD} # 地面站密码
export GCS_USERNAME=${GCS_USERNAME} # 地面站用户名
export GCS_IP=${GCS_IP} # 地面站IP
export NAS_PATH=${NAS_PATH} " | sudo tee ${logpush_env}
    echo "true" > ./.logpush_status
    sudo cp /opt/qomolo/utils/qomolo_gcs_scripts/log/.env \
        /opt/qomolo/utils/qomolo_gcs_scripts/log/env
    fi
}

BYNAV_LOG()
{
    # if 105 
    if [ $(yq '.host_id' ${GLOBAL_PROFILE}) -eq 1 ];then
        sudo bash /opt/qomolo/utils/beiyun_log/scripts/set_bynavlogservice.bash
    else
        tLogger "skip bynav log service deploy" W
    fi
}

BASHRC_EXIST()
{
    if [ $(env | grep PATH | grep qpilot_setup | wc -l) -ne 1 ];then
        echo "export PATH=$PATH:/opt/qomolo/utils/qomolo_gcs_scripts/tools/:/opt/qomolo/utils/qpilot_setup/tools/scripts" >> ~/.bashrc
    fi 
}

QPILOT_ENV()
(
    local env="/opt/qomolo/utils/qpilot_setup/2.10/.env"
    sudo sed -i "s/QOMOLO_ROBOT_ID=.*/QOMOLO_ROBOT_ID=${QOMOLO_ROBOT_ID}/g" ${env}
    sudo sed -i "s/ROS_DOMAIN_ID=.*/ROS_DOMAIN_ID=$(yq ".vehicle_id" ${GLOBAL_PROFILE})/g" ${env}
    sudo sed -i "s#IMAGE=.*#IMAGE=harbor.qomolo.com/arm64/jp51-focal-runtime#g" ${env}
    sudo sed -i "s#DEBUG_WS_PATH=.*#DEBUG_WS_PATH= /data/code/all_ws/ws#g" ${env}
    sudo sed -i "s/ROS_WORKSPACE=.*/ROS_WORKSPACE=qpilot-orin/g" ${env}
)

HW_PARAM()
{
    echo "PROJECT_NAME: ${PROJECT_NAME}"
    echo "QOMOLO_ROBOT_ID: ${QOMOLO_ROBOT_ID}"
    /opt/qomolo/utils/qpilot_setup/tools/scripts/qomolo-param-deploy 
}

# ---------- check deploy result ----------
# 格式化输出
_output_msg_format()
{
    _RED='\033[0;31m'      # ERROR
    _GREEN='\033[0;32m'    # INFO
    _YELLOW='\033[0;33m'   # WARN
    _NC='\033[0m'          # NORMAL
    case "${1}" in
    0) printf "%-64s ${_GREEN}%-15s${_NC}%-20s\n" ${2} "install"   ${3};;
    *) printf "%-64s ${_RED}%-15s${_NC}%-20s\n" ${2} "uninstall" ${3};;
    esac
}
# 判断deb是否存在
_check_deb_ifexist_and_version()
{
    dpkg -s ${1} > /dev/null 2>&1
    case $? in
    0)
        case $(dpkg -s ${1} | grep Status | awk '{print$2}') in
        "install") echo "0" "$(dpkg -s ${1} | grep Version | awk '{print$2}')" ;;
        *)  echo "1" "" ;;
        esac ;;
    *) echo "1" "" ;;
    esac
}
# 判断cmd是否存在
_check_cmd_ifexist()
{
    command -v $1 > /dev/null 2>&1
    echo $?
}


debs_version_check()
{
    echo -e "\033[31mCheck_Program[cmd/deb]:\033[0m\t\t\t\t\t\t \033[31mResult:\033[0m\t\033[31mVersion:\033[0m"
    for i in $(cat ${config});do
        ret=$(_check_deb_ifexist_and_version ${i})
        _output_msg_format "${ret:0:1}" "deb:${i}" "${ret:1}"
    done
}

cmd_version_check()
{
    tLogger "waiting ..." W
}

# ---------- tools ----------
tCheck()
{   # check 
    debs_version_check
    cmd_version_check
}

tPrefixCheck()
{
    local file=${1}
    case ${NetStats} in
    "online")
        if [ "${file}" == "${config}" ];then
            return 0;
        fi ;;
    *)
        if [ ! -f ${file} ];then
            tLogger "${file} not exist!" F
        fi ;;
    esac
} 
tLogger()
{
    _RED='\033[0;31m'      # ERROR
    _GREEN='\033[0;32m'    # INFO
    _YELLOW='\033[0;33m'   # WARN
    _NC='\033[0m'          # NORMAL
    case "${2}" in
    "E") 
    echo '+===========================================================+'
    printf "${_RED}  --> ${1}.${_NC}\n"
    echo '+===========================================================+' ;;
    "F") 
    echo '+===========================================================+'
    printf "${_RED}  --> ${1}, program exit.${_NC}\n"
    echo '+===========================================================+'; exit 1 ;;
    "I") 
    echo '+===========================================================+'
    printf "${_GREEN}  --> ${1}.${_NC}\n"
    echo '+===========================================================+' ;;
    "W") 
    echo '+===========================================================+'
    printf "${_YELLOW}  --> ${1}.${_NC}\n"
    echo '+===========================================================+' ;;
    "N"|""|*) 
    echo '+===========================================================+'
    printf "  --> ${1}.${_NC}\n"
    echo '+===========================================================+' ;;
    esac
}
# ---------- main ---------- 
tPrefixCheck ${config}
tPrefixCheck ${GLOBAL_PROFILE}
tPrefixCheck ${PROJECT_PROFILE}
tPrefixCheck ${VEHICLE_PROFILE}

case "${opts}" in
"offline") ;;
"online") opts= ;;
"check") tCheck; exit 0 ;;
*) USAGE ; exit 0 ;;
esac 

main()
{   # main
    INSTALL_DEBS
    CAN_CONFIG_CHECK
    BYNAV_LOG
    BASHRC_EXIST
    QPILOT_ENV
    HW_PARAM
    LOGPUSH_CONFIG
}; main