#!/usr/bin/env bash

docker stop A006 && docker rm A006

xhost +

echo "Checking whether we are running as root"
if [ "$(id -u)" -ne 0 ]; then
  echo
else
  echo "Please DO NOT run the build script as root"
  exit
fi

docker run -it -d \
  --privileged=true \
  --gpus all \
  --net host \
  --name A006 \
  -p 8080:8080 \
  -e NVIDIA_DRIVER_CAPABILITIES=compute,utility,graphics \
  -e RMW_IMPLEMENTATION=rmw_cyclonedds_cpp \
  -e QOMOLO_ROBOT_ID=A006 \
  -e ROS_DOMAIN_ID=132 \
  -e ROS_MAP_ID=qp \
  -e LOG_PATH=/tmp \
	-e MQTT_NAMESPACE=A006 \
	-e MQTT_SERVER_IP=113.31.113.98 \
	-e MQTT_SERVER_PORT=19000 \
	-e USE_RVIZ=True \
	-e DISPLAY=unix$DISPLAY \
  -e CMAKE_PREFIX_PATH=/opt/third_party/casadi/lib/cmake/casadi:/opt/third_party/ceres/lib/cmake/Ceres:/opt/third_party/osqp-cpp/lib/cmake/:/opt/third_party/abseil-cpp/lib/cmake/:/opt/third_party/osqp/lib/cmake/ \
  -e LD_LIBRARY_PATH=/opt/third_party/pangolin/lib:/opt/third_party/casadi/lib:/opt/opencv/lib/cmake/opencv4:/opt/third_party/osqp-cpp/lib/:/opt/third_party/abseil-cpp/lib/:/opt/third_party/osqp/lib/ \
  -e CPLUS_INCLUDE_PATH=/opt/third_party/osqp/include/ \
	-e ROS_WORKSPACE=qpilot2_ws \
	-e GDK_SCALE \
	-e GDK_DPI_SCALE \
  -e CXX=/usr/bin/g++ \
  -v /tmp:/tmp \
	-v /dev:/dev \
	-v /etc/localtime:/etc/localtime \
	-v /opt/qomolo:/opt/qomolo \
	-v ~:/debug \
  	-w /debug \
  harbor.qomolo.com/ros2/foxy/foxy-focal-runtime \
  /bin/bash
