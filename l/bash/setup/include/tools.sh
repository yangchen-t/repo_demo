#!/bin/bash

tUsages()
{   vQPILOT
    echo "Usage:bash $0 [option]"
    echo "Options:"
    echo -e "\t -f   : skip versio diff check"
    echo -e "\t    --force"
    echo -e "\t -config: only generated supervisor config"
    echo -e "\t    --supervisor"
    echo -e "\t -log : debug create container information"
    echo -e "\t    --information"
    echo -e "\t -i   : enter create ${QPILOT} container"
    echo -e "\t    --into"
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
    "N"|""|*) printf "${2}${_NC}";;
    esac
}

tExitcode()
{
    local _code=$1
    exec >&101-
    sleep 0.02
    exit ${_code}
}

tDebugContainerInformation()
{
   vQPILOT && docker container logs ${QPILOT} -f -n 200
}

tIntoCreateContainer()
{
    vQPILOT && docker container exec -it ${QPILOT} bash; exit -1
}

tDependToolsCheck()
{
    # depend tools check
    if [ ! -f /usr/local/bin/${TOOLS_1} ]; then
        sudo apt update
        sudo apt install ${TOOLS_1} -y
    fi
    if [ ! -f /usr/local/bin/${TOOLS_2} ]; then
        sudo apt update
        sudo apt install qomolo-${TOOLS_2} -y
    fi
}

tGroupVersionDiffCheck()
{
    result=$(QLOG_STD_DISABLED=1 timeout 10s qomolo-get g ${QPILOT_GROUP} --diff)
    case $? in
    1) tLogger W "[Warning]--> Maybe ${QPILOT_GROUP} not install" ;;
    2)
        tLogger E "[Error]--> Found some erros, program stop"
        echo "${result}";exit -1 ;;
    124) tLogger W "[Ignore]--> Check timeout, skip check ${QPILOT_GROUP}" ;;
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
    tLogger I "即将启动的group版本是 ${GROUP_VERSION}"
}

# defalut autostart = true
# defalut autorestart = false
tAdjustSupervisorConfigOtherChoose()
{
    _start="autostart"
    _restart="autorestart"
    _default_autostart="true"
    _default_autorestart="false"
    _insert_point="redirect_stderr=true"
    _m_ary=${1:-""}

    module_name=$(echo ${_m_ary} | grep -oP "program:\K\w+" || echo "")

    for i in $(seq 0 $((${2:-0} -1)));do 
        yaml_module=$(yq eval '.qpilot.'"${_vehicle_type}"'-'$((_dcu_count-1))'.dcu'"${_dcu_mark}"'["'"${i}"'"]' ${PROJECT_YAML})
        if [[ $(echo ${yaml_module} | grep -oP "name: \K\w+" ||  echo "") == "${module_name}" ]];then
            autostart=$(echo ${yaml_module} | grep -oP "${_start}: \K\w+" || echo "${_default_autostart}")
            autorestart=$(echo ${yaml_module} | grep -oP "${_restart}: \K\w+" || echo "${_default_autorestart}")
            break
        fi
    done  
    if [[ "$_m_ary" == *"$_insert_point"* ]]; then
        if [[ "$_m_ary" != *"${_start}"* ]];then
            _m_ary=$(echo "${_m_ary}" | sed -E "s/${_insert_point}/${_insert_point}\n${_start}=${autostart}/")
        else
            _m_ary=$(echo "${_m_ary}" | sed -E "s/${_start}=.*/${_start}=${autostart}/")
        fi 
        if [[ "$_m_ary" != *"${_restart}"* ]];then
            _m_ary=$(echo "${_m_ary}" | sed -E "s/${_insert_point}/${_insert_point}\n${_restart}=${autorestart}/")
        else
            _m_ary=$(echo "${_m_ary}" | sed -E "s/${_restart}=.*/${_restart}=${autorestart}/")
        fi
    fi
    echo -e "${_m_ary}\n" >> ${SUPERVISOR_CONFIG}
}

# generate supervisord config
tGeneratedSupervisorConfig()
{
    sudo touch ${SUPERVISOR_CONFIG} >/dev/zero || true
    sudo chown -R nvidia.nvidia ${SUPERVISOR_CONFIG}
    sudo echo "" > ${SUPERVISOR_CONFIG}

    local _vehicle_type=""
    local _dcu_count=${varList["DCU_COUNT"]}
    local _dcu_mark=${varList["HOST"]}
    declare -A _module_map
    case ${varList["VEHICLE_TYPE"]} in
        qt*|ws*|et*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:2} ;;
        igv*|bus*|tug*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:3} ;;
        qthd*|qbus*) _vehicle_type=${varList["VEHICLE_TYPE"]:0:4} ;;
        *) _vehicle_type="igv" ;;
    esac
    local _module_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].name' ${PROJECT_YAML})
    local _real_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].module' ${PROJECT_YAML})
    _array_length=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'| length' ${PROJECT_YAML})

    IFS=$'\n' read -d '' -r -a arr1 <<< "${_module_list}"
    IFS=$'\n' read -d '' -r -a arr2 <<< "${_real_list}"
    for ((i=0; i<${#arr2[@]}; i++)); do
        _module_map[${arr2[i]}]=${arr1[i]}
    done

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

    for key in "${!_module_map[@]}"; do
        _module_config=$(awk "/\[program:${key}\]/,/^$/" ${REFERENCE_SUPERVISORD_CONFIG})
        tAdjustSupervisorConfigOtherChoose "${_module_config}" ${_array_length}
    
        if [[ ${key} != ${_module_map[${key}]} ]];then 
            sudo sed -i "s/\[program:${key}\]/\[program:${_module_map[${key}]}\]/g" ${SUPERVISOR_CONFIG}
        fi
    done
    tLogger I "Generated supervisor config finish"
}