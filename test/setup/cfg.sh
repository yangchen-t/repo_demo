#!/bin/bash

# set -x 

rc="./rc.yaml"
real="./real.yaml"
super="./all.conf"
SUPERVISOR_CONFIG="./super.conf"


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
    remote_control_module=$(yq eval '.qpilot.'"${_vehicle_type}"'-'$((_dcu_count-1))'.dcu'"${_dcu_mark}"'.start[] | select(.name == "'${module_name}'")' ${REMOTE_CONTROL_PROJECT_YAML})
    yaml_module=$(yq eval '.qpilot.'"${_vehicle_type}"'-'$((_dcu_count-1))'.dcu'"${_dcu_mark}"'[] | select(.name == "'${module_name}'")' ${PROJECT_YAML})
    yaml_module_m=$(echo ${yaml_module} | grep -oP "module: \K\w+" ||  echo "")
    remote_control_module_m=$(echo ${remote_control_module} | grep -oP "module: \K\w+" ||  echo "")

    if [[ ${yaml_module_m} == "${module_name}" ]] ;then
        autostart=$(echo ${yaml_module} | grep -oP "${_start}: \K\w+" || echo "${_default_autostart}")
        autorestart=$(echo ${yaml_module} | grep -oP "${_restart}: \K\w+" || echo "${_default_autorestart}")
    elif [[ ${remote_control_module_m} == "${module_name}" ]];then
        autostart="false"; autorestart="false"
    fi
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

    echo -e "${_m_ary}\n" >> ${SUPERVISOR_CONFIG}
}

# generate supervisord config
tGeneratedSupervisorConfig()
{
    if [ ! -f ${SUPERVISOR_CONFIG} ];then
        sudo touch ${SUPERVISOR_CONFIG} >/dev/zero || true
    fi 
    sudo chown -R westwell.westwell ${SUPERVISOR_CONFIG}
    sudo echo "" > ${SUPERVISOR_CONFIG}
    if [ ! -s ${real} ];then
        echo "${real} maybe is empty, Running doesn't make any sense, stop..."; exit -1
    fi

    local _vehicle_type="igv"
    local _dcu_count=2
    local _dcu_mark=1
    declare -A _module_map

    local _module_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].name' ${real})
    local _real_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].module' ${real})
    _array_length=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'| length' ${real})

    IFS=$'\n' read -d '' -r -a setup1 <<< "${_module_list}"
    IFS=$'\n' read -d '' -r -a setup2 <<< "${_real_list}"
    START_MODE="defalut"
    if [[ ${START_MODE} == "defalut" ]];then 
        if [ -e ${rc} ] && [ -s ${rc} ];then
            if [ ! -s ${rc} ];then
                echo W "${real} maybe is empty ?"
            fi
            local _remote_module_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'.start[].name' ${rc})
            local _remote_real_list=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'.start[].module' ${rc})
            _remote_array_length=$(yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'.start| length' ${rc})
            IFS=$'\n' read -d '' -r -a remote_control1 <<< "${_remote_module_list}"
            IFS=$'\n' read -d '' -r -a remote_control2 <<< "${_remote_real_list}"
            setup1=("${setup1[@]}" "${remote_control1[@]}")
            setup2=("${setup2[@]}" "${remote_control2[@]}")
            _array_length=$(( _array_length + _remote_array_length ))
        fi
    fi

    for ((i=0; i<${#setup2[@]}; i++)); do
        echo ${setup2[i]} ${setup1[i]}
        _module_map[${setup2[i]}]=${setup1[i]}
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
        _module_config=$(awk "/\[program:${key}\]/,/^$/" ${super})

        tAdjustSupervisorConfigOtherChoose "${_module_config}"
    
        if [[ ${key} != ${_module_map[${key}]} ]];then 
            sudo sed -i "s/\[program:${key}\]/\[program:${_module_map[${key}]}\]/g" ${SUPERVISOR_CONFIG}
        fi
    done
    echo I "generated supervisor config finish"
}

# replace()
# {
#     _start="autostart"
#     _restart="autorestart"
#     _autostart="true"
#     _autorestart="false"
#     _insert_point="redirect_stderr=true"
#     _moduel_=${1:-""}
#     module_name=$(echo ${_moduel_} | grep -oP "program:\K\w+" || echo "")
#     rp=$(yq eval '.qpilot."igv-1".dcu1[] | select(.module == "module_name")' ${real})
#     case ${rp} in 
#     *"${_start}"*) 
#         _autostart=$(yq eval '.qpilot."igv-1".dcu1[] | select(.name == "${module_name}")' real.yaml | grep "_start") 
#         _autostart=$(sed -i "s/${_autostart}/autorestart=true/g" ${_autostart})
#     ;;
#     *"${_restart}"*) 
#         break
#     ;;
#     easc
# }

tGeneratedSupervisorConfig