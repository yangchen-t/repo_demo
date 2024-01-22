#!/bin/bash

readonly PROJECT=$1
readonly QOMOLO_ROBOT_ID=$2
readonly WORKSPACE="qpilot"
readonly FILE=("perception.yaml" "lidar_preprocess.yaml")
readonly SRC=("/opt/qomolo/${WORKSPACE}/temp/parameter/profile/perception/" \
            "/opt/qomolo/${WORKSPACE}/temp/parameter/profile/perception/${PROJECT}" \
            "/opt/qomolo/${WORKSPACE}/temp/parameter/profile/perception/${PROJECT}/${QOMOLO_ROBOT_ID}")
readonly DST="/opt/qomolo/qpilot-hw-param/perception/"
readonly USER="qpilot"

if [ ! ${PROJECT} ] || [ ! ${QOMOLO_ROBOT_ID} ];then
    echo "need two args"
    echo "e.g. $0 ica ica1"
    exit -1
fi 

function Unlock()
{
    qomolo-igv_passwd ${USER}
    sleep 1
}
function CleanOldFile()
{
    local file=$(echo $1 | awk -F "/" '{print substr($0,54)}')
    newPath=${DST}${file}
    if [ -f  ${newPath} ];then
        sudo rm -rv ${newPath}
    fi
}

function main()
{
    for path in ${SRC[*]};
    do
        for i in ${FILE[*]};
        do
            CleanOldFile ${path}/${i}
        done
    done 
}

Unlock
main
echo "完成"