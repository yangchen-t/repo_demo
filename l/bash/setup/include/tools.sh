#!/bin/bash

tUsages()
{
    echo "Usage:bash $0 [option]"
    echo "Options:"
    echo -e "\t -f     : skip versio diff check"
    echo -e "\t\t--force     : skip versio diff check"
    echo -e "\t -config: only generated supervisor config"
    echo -e "\t\t--supervisor: only generated supervisor config"
}

tLogger()
{
    _RED='\033[0;31m'      # ERROR
    _GREEN='\033[0;32m'    # INFO
    _YELLOW='\033[0;33m'   # WARN
    _NC='\033[0m'          # NORMAL
    case "${1}" in
    "E") printf "${_RED}${2}${_NC}\n";;        
    "I") printf "${_GREEN}${2}${_NC}\n";;
    "W") printf "${_YELLOW}${2}${_NC}\n";;
    *|"N") printf "${2}${_NC}";;
    esac
}

tExitcode()
{
    local _code=$1
    exec >&101-
    sleep 0.02
    exit ${_code}
}

tDependToolsCheck()
{
    # depend check
    if [ ! -f /usr/local/bin/${TOOLS_1} ]; then
        sudo apt update
        sudo apt install ${TOOLS_1} -y
    fi
    if [ ! -f /usr/local/bin/${TOOLS_2} ]; then
        sudo apt update
        sudo apt install qomolo-${TOOLS_2} -y
    fi
}

tGroupVersionDiffCheck() {

    result=$(QLOG_STD_DISABLED=1 timeout 10s qomolo-get g ${QPILOT_GROUP} --diff)
    case $? in
    1)
        tLogger W "[Warning]--> Maybe ${QPILOT_GROUP} not install"
        ;;
    2)
        tLogger E "[Error]--> Found some erros, program stop"
        echo "${result}";exit -1
        ;;
    124)
        tLogger W "[Ignore]--> Check timeout, skip check ${QPILOT_GROUP}"
        ;;
    esac
}

tGroupVersionGet()
{
    local _QPILOT_GROUP=$(qomolo-get g ${QPILOT_GROUP} --cur --format json | yq eval '.version')
    if ! [[ "${_QPILOT_GROUP}" =~ ^[0-9]+(\.[0-9]+)+(\.[0-9999]+)+$ ]]; then
        GROUP_VERSION=$(dpkg -l | grep ${QPILOT} | head -n 1 | awk '{print $3}')
    else
        GROUP_VERSION=${_QPILOT_GROUP}
    fi
    tLogger I "现在即将启动的group版本是 ${GROUP_VERSION}"
}

# generate supervisord config
tConfigGenerated()
{
    sudo chown -R nvidia.nvidia ${SUPERVISOR_CONFIG}
    sudo echo "" > ${SUPERVISOR_CONFIG}
    local _vehicle_type=""
    local _dcu_count=${varList["DCU_COUNT"]}
    local _dcu_mark=${varList["HOST"]}
    case ${varList["VEHICLE_TYPE"]} in
        qt*|ws*|et*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:2} ;;
        igv*|bus*|tug*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:3} ;;
        qthd*|qbus*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:4} ;;
    esac
    local _module_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].name' ${PROJECT_YAML})
    local _real_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].module' ${PROJECT_YAML})
    declare -A _module_map

    # prefix 
    cat > ${SUPERVISOR_CONFIG} << EOF
[inet_http_server]
chmod=0777
chown=nobody:nogroup
port=0.0.0.0:9001
username=qomolo
password=123

[supervisord]
nodaemon=true

EOF

    IFS=$'\n' read -d '' -r -a arr1 <<< "${_module_list}"
    IFS=$'\n' read -d '' -r -a arr2 <<< "${_real_list}"
    for ((i=0; i<${#arr2[@]}; i++)); do
        _module_map[${arr2[i]}]=${arr1[i]}
    done

    for key in "${!_module_map[@]}"; do
        sudo awk "/\[program:${key}\]/,/^$/" ${REFERENCE_SUPERVISORD_CONFIG} >> ${SUPERVISOR_CONFIG}
        if [[ ${key} != ${_module_map[${key}]} ]];then
            sudo sed -i "s/\[program:${key}\]/\[program:${_module_map[${key}]}\]/g" ${SUPERVISOR_CONFIG}
        fi
    done
}