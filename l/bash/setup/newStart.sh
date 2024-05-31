#!/bin/bash

SETUP_MODE=${SETUP_MODE:-"info"}
if [[ "${SETUP_MODE}" == "debug" ]]; then
    set -x  # DebugMode
fi  # export SETUP_MODE="debug"

# set -e  # ReturnZeroExit
set -u  # NullVarCheck
set -o pipefail

readonly WORKING_PATH="/opt/qomolo/utils/qpilot_setup/2.10"

# include 
source ${WORKING_PATH}/include/tools.sh
source ${WORKING_PATH}/include/variable.sh


_Initialize() {

    tDependToolsCheck
    if [ ! -d "${WORKSPACE}/coredump" ]; then
        sudo mkdir -p ${WORKSPACE}/coredump
    fi
    if [ ! -d "${WORKSPACE}/csv" ]; then
        sudo mkdir -p ${WORKSPACE}/csv
    fi
    if [ ! -d "${WORKSPACE}/igv_log" ]; then
        sudo mkdir -p ${WORKSPACE}/igv_log
    fi
}

DcokerCreate() {
    
    _Initialize
    case ${OPTIONS} in
    "-log"|"--information") tDebugContainerInformation ;;
    "-i"|"--into") tIntoCreateContainer ;;
    "-config"|"--supervisor") vCheckStartVar && tLogger W "use config ${SUPERVISOR_CONFIG}" && exit -1;;
    "-f"|"--force") tLogger W "skip version diff check" && vCheckStartVar ;;
    "defalut") vCheckStartVar && tGroupVersionDiffCheck  ;;
    *) tUsages && exit -1 ;;
    esac
    tGroupVersionGet

    tLogger I "workspace: ${WORKING_PATH}"
    tLogger I "conf     : ${SUPERVISOR_CONFIG}"
    tLogger I "images   : ${IMAGE}"
    docker container kill ${QPILOT} &> /dev/zero || true
    docker container stop ${QPILOT} &> /dev/zero || true
    docker container rm $(docker ps -a | grep  ${QPILOT} | awk '{print$1}') &> /dev/zero  || true

    xhost +
    docker run -it \
        --restart=always \
        -d \
        --gpus all \
        --privileged=true \
        --network=host \
        --name ${QPILOT} \
        -e DISPLAY=unix${DISPLAY} \
        -e QT_GRAPHICSSYSTEM=native \
        -e NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
        -e GDK_SCALE \
        -e GDK_DPI_SCALE \
        -v /tmp/.X11-unix:/tmp/.X11-unix \
        -v /dev:/dev \
        -e QOMOLO_CONFIGURATION_PATH="/opt/qomolo/${QPILOT}/share/qpilot_parameters" \
        -e QOMOLO_ROBOT_ID=${QOMOLO_ROBOT_ID} \
        -e ROS_DOMAIN_ID=${varList["VEHICLE_ID"]} \
        -e ROS_WORKSPACE=${QPILOT} \
        -e MQTT_NAMESPACE=${varList["MQTT_NAMESPACE"]} \
        -e MQTT_SERVER_IP=${varList["MQTT_SERVER_IP"]} \
        -e MQTT_SERVER_PORT=${varList["MQTT_SERVER_PORT"]} \
        -e FMS_COMMON_IP=${varList["FMS_COMMON_IP"]} \
        -e FMS_COMMON_PORT=${varList["FMS_COMMON_PORT"]} \
        -e FMS_TRAJECTORY_PORT=${varList["FMS_TRAJECTORY_PORT"]} \
        -e QOMOLO_MAP_PATH=${varList["QOMOLO_MAP_PATH"]} \
        -e VOC_SERVER_URL=${varList["VOC_SERVER_URL"]} \
        -e QPILOT_VERSION=${GROUP_VERSION} \
        -e ROS_FOXY_VERSION=${ROS_FOXY_VERSION} \
        -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
        -e LOG_PATH=${LOG_PATH} \
        -e CYCLONEDDS_URI=file:///cyclonedds.xml \
        -e FASTRTPS_DEFAULT_PROFILES_FILE=/DEFAULT_FASTRTPS_PROFILES.xml \
        -e TYPE=${TYPE} \
        -e CMAKE_PREFIX_PATH=/opt/third_party/casadi/lib/cmake/casadi:/opt/third_party/ceres/lib/cmake/Ceres:/opt/third_party/osqp-cpp/lib/cmake/:/opt/third_party/abseil-cpp/lib/cmake/:/opt/third_party/osqp/lib/cmake/ \
        -e LD_LIBRARY_PATH=/opt/third_party/pangolin/lib:/opt/opencv/lib/:/opt/third_party/casadi/lib:/opt/opencv/lib/cmake/opencv4:/opt/third_party/osqp-cpp/lib/:/opt/third_party/abseil-cpp/lib/:/opt/third_party/osqp/lib/ \
        -e CPLUS_INCLUDE_PATH=/opt/third_party/osqp/include/ \
        -e PATH=${PATH} \
        -v /opt/qomolo:/opt/qomolo \
        -v /etc/localtime:/etc/localtime \
        -v /etc/miivii_release:/etc/miivii_release \
        -v ${WORKSPACE}:/debug \
        -v /data/key_log:/key_log \
        -v /data/key_log/save_images:/data/save_images  \
        -v /run/systemd/:/run/systemd/ \
        -v ${WORKING_PATH}/conf/tester_for_usb.launch_ceke.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_usb.launch_ceke.py \
        -v ${WORKING_PATH}/conf/tester_for_usb.launch_tj.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_usb.launch_tj.py \
        -v ${WORKING_PATH}/conf/tester_for_eth.launch.py:/opt/ros/foxy/share/novatel_gps_driver/launch/tester_for_eth.launch.py \
        -v ${WORKING_PATH}/conf/cyclonedds.xml:/cyclonedds.xml \
        -v ${WORKING_PATH}/conf/DEFAULT_FASTRTPS_PROFILES.xml:/DEFAULT_FASTRTPS_PROFILES.xml \
        -v ${SUPERVISOR_CONFIG}:/etc/supervisor/conf.d/supervisord.conf \
        -v ${WORKING_PATH}/scripts:/scripts \
        -v /etc/qomolo/profile:/etc/qomolo/profile \
        -w /debug \
        ${IMAGE} bash -c "sysctl -p; /usr/bin/supervisord"
        echo "$(date -u '+%Z %F %T.%3N') -> $(date +%s)" >&101 && tExitcode 0
}
DcokerCreate