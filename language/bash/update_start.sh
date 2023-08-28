#!/bin/bash

WORKING_PATH=$(dirname $(realpath $0))
source ${WORKING_PATH}/.env

readonly QPILOT_NAME="qpilot-group"
readonly TOOLS_1="qomolo-get"
readonly TOOLS_2="yq"

readonly GLOBAL_PROFILE="/etc/qomolo/profile/global/profile.yaml"
readonly PROJECT_PROFILE="/etc/qomolo/profile/project/profile.yaml"
readonly VEHICLE_PROFILE="/etc/qomolo/profile/vehicle_type/profile.yaml"
readonly QPILOT="qpilot"
readonly QOMOLO_CONFIGURATION_PATH="/opt/qomolo/${QPILOT}/share/qpilot_parameters"
readonly WORKSPACE="/data/code/all_ws/ws/"
readonly LOG_PATH="/debug/csv/"
readonly IMAGE="harbor.qomolo.com/arm64/xvaier-focal-runtime"
readonly TYPE="RELEASE"

MQTT_NAMESPACE=$(yq ".MQTT_NAMESPACE" ${PROJECT_PROFILE})
MQTT_SERVER_IP=$(yq ".MQTT_SERVER_IP" ${PROJECT_PROFILE})
MQTT_SERVER_PORT=$(yq ".MQTT_SERVER_PORT" ${PROJECT_PROFILE})
FMS_COMMON_IP=$(yq ".FMS_COMMON_IP" ${PROJECT_PROFILE})
FMS_COMMON_PORT=$(yq ".FMS_COMMON_PORT" ${PROJECT_PROFILE})
FMS_TRAJECTORY_PRY_PORT=$(yq ".FMS_TRAJECTORY_PRY_PORT" ${PROJECT_PROFILE})
QOMOLO_MAP_PATH=$(yq ".QOMOLO_MAP_PATH" ${PROJECT_PROFILE})
VOC_SERVER_URL=$(yq ".VOC_SERVER_URL" ${PROJECT_PROFILE})
PROJECT_NAME=$(yq ".profile_name" ${PROJECT_PROFILE})
VEHICLE_TYPE=$(yq ".profile_name" ${VEHICLE_PROFILE})
VEHICLE_ID=$(yq ".vehicle_id" ${GLOBAL_PROFILE})

case ${VEHICLE_TYPE} in
qt*)
    VEHICLE_TYPE=Q_
    ;;
igv*)
    VEHICLE_TYPE=
    ;;
ws*)
    VEHICLE_TYPE=W_
    ;;
bus*)
    VEHICLE_TYPE=B_
    ;;
esac

case ${PROJECT_NAME} in
cnwxijk)
    PROJECT=jk
    ;;
esac

# check group
function Check() {
    if [ ! -f /usr/local/bin/${TOOLS_1} ]; then
        sudo apt update
        sudo apt install ${TOOLS_1} -y
    fi
    if [ ! -f /usr/local/bin/${TOOLS_2} ]; then
        sudo apt update
        sudo apt install qomolo-${TOOLS_2} -y
    fi
    result=$(QLOG_STD_DISABLED=1 timeout 10s qomolo_get g ${QPILOT_NAME} --diff)
    case $? in
    1)
        echo -e "\033[33m[Warning]: Maybe ${QPILOT_NAME} not install \033[0m"
        ;;
    2)
        echo -e "\033[31m[Error]: Found some erros, program suspension\033[0m"
        echo ${result}
        exit -1
        ;;
    124)
        echo -e "\033[33m[Ignore]: Check timeout, skip check ${QPILOT_NAME} \033[0m"
        ;;
    esac
}

function Init() {
    xhost +
    if [ ! -d "${WORKSPACE}/coredump" ]; then
        sudo mkdir -p ${WORKSPACE}/coredump
    fi
    if [ ! -d "${WORKSPACE}/csv" ]; then
        sudo mkdir -p ${WORKSPACE}/csv
    fi
    if [ ! -d "${WORKSPACE}/igv_log" ]; then
        sudo mkdir -p ${WORKSPACE}/igv_log
    fi
    if [ ! -d "${WORKSPACE}/qpilot_log" ]; then
        sudo mkdir -p ${WORKSPACE}/qpilot_log
    fi
    # hardware.dcu > host_id
    DCU_COUNT=$(yq ".hardware.dcu | length" ${VEHICLE_PROFILE})
    if [[ ${DCU_COUNT} == 3 ]]; then
        HOST=$(yq ".host_id" ${GLOBAL_PROFILE})
        if [[ ${HOST} == 1 ]]; then
            DEVICE=105
            SUPER=${VEHICLE_TYPE}${PROJECT}_supervisor_${DEVICE}_2.10.conf
        else
            DEVICE=106
            SUPER=${VEHICLE_TYPE}${PROJECT}_supervisor_${DEVICE}_2.10.conf
        fi
    else
        SUPER=${VEHICLE_TYPE}${PROJECT}_supervisor_2.10.conf
    fi
    echo -e "\033[34mconf:\033[0m" ${WORKING_PATH}/conf/${SUPER}
    if [[ ! -f ${WORKING_PATH}/conf/${SUPER} ]]; then
        echo -e "\033[31m current supervisor conf is not exist \033[0m"
        exit -1
    fi
}
# -e QOMOLO_ROBOT_ID=${PROJECT}${VEHICLE_ID} \
function Start() {
    echo -e "\033[34mworkspace:\033[0m" $WORKING_PATH
    docker container stop qpilot || true
    docker container rm qpilot || true

    QPILOT_VERSION=$(dpkg -l | grep ${QPILOT} | head -n 1 | awk '{print $3}')
    echo "现在即将启动的qpilot 版本是${QPILOT_VERSION}"

    docker run -it \
        --restart=always \
        -d \
        --gpus all \
        --privileged=true \
        --network=host \
        --name qpilot \
        -e DISPLAY=unix$DISPLAY \
        -e QT_GRAPHICSSYSTEM=native \
        -e NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
        -e GDK_SCALE \
        -e GDK_DPI_SCALE \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v /dev:/dev \
        -e QOMOLO_CONFIGURATION_PATH=${QOMOLO_CONFIGURATION_PATH} \
        -e QOMOLO_ROBOT_ID=${QOMOLO_ROBOT_ID} \
        -e ROS_DOMAIN_ID=${VEHICLE_ID} \
        -e ROS_WORKSPACE=${QPILOT} \
        -e MQTT_NAMESPACE=${MQTT_NAMESPACE} \
        -e MQTT_SERVER_IP=${MQTT_SERVER_IP} \
        -e MQTT_SERVER_PORT=${MQTT_SERVER_PORT} \
        -e FMS_COMMON_IP=${FMS_COMMON_IP} \
        -e FMS_COMMON_PORT=${FMS_COMMON_PORT} \
        -e FMS_TRAJECTORY_PORT=${FMS_TRAJECTORY_PORT} \
        -e QOMOLO_MAP_PATH=${QOMOLO_MAP_PATH} \
        -e VOC_SERVER_URL=${VOC_SERVER_URL} \
        -e QPILOT_VERSION=${QPILOT_VERSION} \
        -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
        -e LOG_PATH=${LOG_PATH} \
        -e CYCLONEDDS_URI=file:///cyclonedds.xml \
        -e FASTRTPS_DEFAULT_PROFILES_FILE=/DEFAULT_FASTRTPS_PROFILES.xml \
        -e TYPE=${TYPE} \
        -e CMAKE_PREFIX_PATH=/opt/third_party/casadi/lib/cmake/casadi:/opt/third_party/ceres/lib/cmake/Ceres:/opt/third_party/osqp-cpp/lib/cmake/:/opt/third_party/abseil-cpp/lib/cmake/:/opt/third_party/osqp/lib/cmake/ \
        -e LD_LIBRARY_PATH=/opt/third_party/pangolin/lib:/opt/opencv/lib/:/opt/third_party/casadi/lib:/opt/opencv/lib/cmake/opencv4:/opt/third_party/osqp-cpp/lib/:/opt/third_party/abseil-cpp/lib/:/opt/third_party/osqp/lib/ \
        -e CPLUS_INCLUDE_PATH=/opt/third_party/osqp/include/ \
        -e PATH=$PATH \
        -v /opt/qomolo:/opt/qomolo \
        -v /etc/localtime:/etc/localtime \
        -v ${WORKSPACE}:/debug \
        -v /data/key_log:/key_log \
        -v ${WORKING_PATH}/conf/tester_for_usb.launch_ceke.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_usb.launch_ceke.py \
        -v ${WORKING_PATH}/conf/tester_for_usb.launch_tj.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_usb.launch_tj.py \
        -v ${WORKING_PATH}/conf/tester_for_eth.launch.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_eth.launch.py \
        -v ${WORKING_PATH}/conf/cyclonedds.xml:/cyclonedds.xml \
        -v ${WORKING_PATH}/conf/DEFAULT_FASTRTPS_PROFILES.xml:/DEFAULT_FASTRTPS_PROFILES.xml \
        -v ${WORKING_PATH}/conf/${SUPER}:/etc/supervisor/conf.d/supervisord.conf \
        -v ${WORKING_PATH}/scripts:/scripts \
        -w /debug \
        ${IMAGE} bash -c "sysctl -p; /usr/bin/supervisord"
}

if [[ $1 == "-f" ]]; then
    Init
    Start
else
    Check
    Init
    Start
fi
