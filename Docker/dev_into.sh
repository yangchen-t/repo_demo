#!/usr/bin/env bash

echo "Checking whether we are running as root"
if [ "$(id -u)" -ne 0 ]; then
  echo
else
  echo "Please DO NOT run the build script as root"
  exit
fi

docker exec -it qpilot2.${QOMOLO_ROBOT_ID} /bin/bash