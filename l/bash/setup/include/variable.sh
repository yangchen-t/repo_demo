#!/bin/bash

source ${WORKING_PATH}/.env &> /dev/zero

exec 101> >( sed -u 's/\r/\r\t\t\t\t\t\t\t/g' | logger -p local0.info -t $0 )

declare -A varList

readonly TOOLS_1="qomolo-get"
readonly TOOLS_2="yq"

readonly GLOBAL_PROFILE="/etc/qomolo/profile/global/profile.yaml"
readonly PROJECT_PROFILE="/etc/qomolo/profile/project/profile.yaml"
readonly VEHICLE_PROFILE="/etc/qomolo/profile/vehicle_type/profile.yaml"
readonly IMAGE_VERSION_PROFILE="/opt/qomolo/utils/qpilot_image/VERSION.json"
readonly QPILOT_GROUP="qpilot-group"
readonly WORKSPACE="/data/code/all_ws/ws/"
readonly LOG_PATH="/debug/csv/"
readonly TYPE="RELEASE"
readonly tmpversion="_2.10"
# readonly OSM="/opt/qomolo/qpilot-resource/planning/map/qp.osm"
readonly PROJECT_YAML="/etc/qomolo/profile/qpilot/setup/profile.yaml"
readonly REFERENCE_SUPERVISORD_CONFIG="/opt/qomolo/qpilot-config/setup/all_supervisord.conf"
SUPERVISOR_CONFIG="${WORKING_PATH}/supervisord.conf"

OPTIONS=${1:-"defalut"}
DISPLAY=${DISPLAY:-"0"}


vProfileCheck() {
    if [ ! -f $1 ]; then
        tLogger E "$1 is not exist";exit -1
    fi
}

vGetImageElement()
{
    if [ ! -f "${IMAGE_VERSION_PROFILE}" ];then
        echo "null";return
    fi
	cat ${IMAGE_VERSION_PROFILE} | yq eval ".${1}" -
}

vQPILOT()
{
    if [ ${ROS_WORKSPACE} ];then
        QPILOT=${ROS_WORKSPACE}
    else
        QPILOT="qpilot-orin"
    fi
}

vCheckStartVar()
{
    vProfileCheck ${GLOBAL_PROFILE}
    vProfileCheck ${PROJECT_PROFILE}
    vProfileCheck ${VEHICLE_PROFILE}

    varList=(
        ["MQTT_NAMESPACE"]=$(yq ".MQTT_NAMESPACE" ${PROJECT_PROFILE})
        ["MQTT_SERVER_IP"]=$(yq ".MQTT_SERVER_IP" ${PROJECT_PROFILE})
        ["MQTT_SERVER_PORT"]=$(yq ".MQTT_SERVER_PORT" ${PROJECT_PROFILE})
        ["FMS_COMMON_IP"]=$(yq ".FMS_COMMON_IP" ${PROJECT_PROFILE})
        ["FMS_COMMON_PORT"]=$(yq ".FMS_COMMON_PORT" ${PROJECT_PROFILE})
        ["FMS_TRAJECTORY_PORT"]=$(yq ".FMS_TRAJECTORY_PORT" ${PROJECT_PROFILE})
        ["QOMOLO_MAP_PATH"]=$(yq ".QOMOLO_MAP_PATH" ${PROJECT_PROFILE})
        ["VOC_SERVER_URL"]=$(yq ".VOC_SERVER_URL" ${PROJECT_PROFILE})
        ["PROJECT_NAME"]=$(yq ".profile_name" ${PROJECT_PROFILE})
        ["VEHICLE_TYPE"]=$(yq ".profile_name" ${VEHICLE_PROFILE})
        ["VEHICLE_ID"]=$(yq ".vehicle_id" ${GLOBAL_PROFILE})
        ["DCU_COUNT"]=$(yq ".hardware.dcu | length" ${VEHICLE_PROFILE})
        ["HOST"]=$(yq ".host_id" ${GLOBAL_PROFILE})
    )

    vQPILOT

    local filename=/opt/qomolo/utils/qpilot_setup/2.10/.project_name
    if [ -f $filename ]; then
        if [ $(wc -l < "$filename") -gt 0 ]; then
            varList["PROJECT_NAME"]=$(cat $filename)
        fi
    fi

    case ${varList["PROJECT_NAME"]} in
        cnwxijk) varList["PROJECT_NAME"]=jk ;;
        mxvlkica) varList["PROJECT_NAME"]=ica ;;
        cnelh) varList["PROJECT_NAME"]=eh ;;
        cnalsck) varList["PROJECT_NAME"]=ck ;;
        cnwha) varList["PROJECT_NAME"]=wh ;;
        cndlidct) varList["PROJECT_NAME"]=dlqt ;;
        cnshaqp) varList["PROJECT_NAME"]=qp ;;
        cntjic) varList["PROJECT_NAME"]=tj ;;
    esac

    # HACK tmp : .env > qprofile
    # qomolo_robot_id
    if [ ! ${QOMOLO_ROBOT_ID} ];then
        varList["PROJECT_NAME"]=$(yq ".profile_name" ${PROJECT_PROFILE})
        QOMOLO_ROBOT_ID=${varList["PROJECT_NAME"]}${varList["VEHICLE_ID"]}
    fi
    # mqtt_namespace
    if [ ${MQTT_NAMESPACE} ];then
        varList["MQTT_NAMESPACE"]=${MQTT_NAMESPACE}
    else
        varList["VEHICLE_ID"]=$(yq ".vehicle_id" ${GLOBAL_PROFILE})
        varList["MQTT_NAMESPACE"]="${varList["MQTT_NAMESPACE"]}$(printf "%02d" ${varList["VEHICLE_ID"]})"
    fi
    # ros_domain_id
    if [ ${ROS_DOMAIN_ID} ];then
        varList["VEHICLE_ID"]=${ROS_DOMAIN_ID}
    fi
    # ros-foxy-version
    if [[ ${IMAGE} != "harbor.qomolo.com/arm64/xvaier-focal-runtime" ]];then
        ROS_FOXY_VERSION=0.3.11
    fi
    # basic images
    local _image=$(vGetImageElement "image")
    local _tag=$(vGetImageElement "tag")
    local _image_id=$(vGetImageElement "image_id")
    if [[ "${_image}" != "null" ]] && [[ "${_tag}" != "null" ]];then
        IMAGE=${_image}:${_tag}
    else
        if [ ${IMAGE} ];then
            IMAGE=${IMAGE}
        else
            IMAGE="harbor.qomolo.com/arm64/jp51-focal-runtime"
        fi
    fi
    vAutoChangeSupervisorConfig
}

vAutoChangeSupervisorConfig()
{
    if [ -f ${PROJECT_YAML} ] && [ -f ${REFERENCE_SUPERVISORD_CONFIG} ];then
        tGeneratedSupervisorConfig; return 0
    fi
    SUPERVISOR_CONFIG=${WORKING_PATH}/conf/
    case ${varList["VEHICLE_TYPE"]} in
        qt*) VEHICLE_PREFIX=Q_ ;;
        igv*) VEHICLE_PREFIX= ;;
        ws*) VEHICLE_PREFIX=W_ ;;
        bus*) VEHICLE_PREFIX=B_ ;;
        tug*) VEHICLE_PREFIX=T_ ;;
    esac
    
    # hardware.dcu > host_id
    if [[ ${varList["DCU_COUNT"]} == 3 ]]; then
        if [[ ${varList["HOST"]} == 1 ]]; then
            DEVICE=105
            SUPER=${VEHICLE_PREFIX}${varList["PROJECT_NAME"]}_supervisor_${DEVICE}${tmpversion}.conf
        else
            DEVICE=106
            SUPER=${VEHICLE_PREFIX}${varList["PROJECT_NAME"]}_supervisor_${DEVICE}${tmpversion}.conf
        fi
    else
        SUPER=${VEHICLE_PREFIX}${varList["PROJECT_NAME"]}_supervisor${tmpversion}.conf
    fi
    if [[ ! -f ${WORKING_PATH}/conf/${SUPER} ]]; then
        T_Logger E "current supervisor conf is not exist"
        exit -1
    fi
    SUPERVISOR_CONFIG+=${SUPER}
}