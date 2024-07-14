#!/bin/bash

set -u

readonly PROJECT_YAML="/etc/qomolo/profile/qpilot/setup/profile.yaml"
readonly VEHICLE_PROFILE="/etc/qomolo/profile/vehicle_type/profile.yaml"
readonly GLOBAL_PROFILE="/etc/qomolo/profile/global/profile.yaml"
readonly prefix="/opt/qomolo/utils/qomolo-yq"

_dcu_count=$(${prefix}/yq ".hardware.dcu | length" ${VEHICLE_PROFILE})
_dcu_mark=$(${prefix}/yq ".host_id" ${GLOBAL_PROFILE})
_vehicle_type=$(${prefix}/yq ".profile_name" ${VEHICLE_PROFILE})



case $(echo $(hostname) | awk -F "-" '{print$2}') in
    igv*|bus*|tug*) _vehicle_type=${_vehicle_type:0:3} ;;
    qthd*|qbus*) _vehicle_type=${_vehicle_type:0:4} ;;
    qt*|ws*|et*) _vehicle_type=${_vehicle_type:0:2} ;;
    *) _vehicle_type="igv" ;;
esac
_module_list=$(${prefix}/yq eval '.qpilot.'"${_vehicle_type}"'-'"$((${_dcu_count}-1))"'.dcu'"${_dcu_mark}"'[].name' ${PROJECT_YAML})

IFS=$'\n' read -d '' -r -a arr1 <<< "${_module_list}"

for ((i=0; i<${#arr1[@]}; i++)); do
    if [[ ${arr1[i]} == "http_bridge" ]] || [[ ${arr1[i]} == "entrypoint_105" ]] || [[ ${arr1[i]} == "entrypoint_106" ]];then
        continue
    fi
    supervisorctl restart ${arr1[i]}
done
supervisorctl stop entrypoint_105 entrypoint_106