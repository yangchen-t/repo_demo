#!/bin/bash

VERSION=$1
PROJECT=$2
DEVICE=$3
TRAILER=$4
PARAM1=''
PARAM2=''
PARAM3=''
PARAM4=''

# check  current premission
if [ "$(id -u)" -ne 0 ]; then
  echo
else
  echo "Please DO NOT run the build script as root"
  exit
fi

function adjust_param()
{
    local version=$1
    local project=$2
    local $device=$3

    case $project in
    tj*|tianjin)
        modify_env $version tj
        modify_conf $version tj 
    ;;
    ck*|ceke)
        modify_env $version ck
        modify_conf $version ck
    ;;
    eh*)
        modify_env $version eh
        modify_conf $version eh
    ;;
    wh*|wuhan)
        modify_env $version wh
        modify_conf $version wh
    ;;
    dl*|dalian)
        modify_env $version dl
        modify_conf $version dl
    ;;
    qp*|qingpu)
        modify_env $version qp
        modify_conf $version qp   
    ;;
    hr*|xm*|xiamen)
        modify_env $version hr
        modify_conf $version hr
    ;;
    jk*|jinke)
        modify_env $version jk
        modify_conf $version jk
    ;;
    jj*|jingjiang)
        modify_env $version jj
        modify_conf $version jj
    ;;
    esac 
}

function modify_conf()
{
    local version=$1
    local project=$2
    local $device=$3
    local supervisorconf=""
    case $version:$project:$device in
    0.8:tj);;
    0.8:)

}

function modify_env()
{
    local version=$1
    local project=$2
    local supervisorconf=""

    if [[ ! -d /opt/qomolo/utils/qpilot_setup/$version/ ]];then
        echo "version dir is not exist"
        exit
    fi
    if [[ ! -f /opt/qomolo/utils/qpilot_setup/$version/.env ]];then
        echo ".env file is not exist"
        exit
    fi 

    cd /opt/qomolo/utils/qpilot_setup/$version/ 
    Location=$(cat -n .env | grep "QOMOLO_ROBOT_ID" | awk '{print$1}')
    if [[ $Location == "" ]];then
        echo "QOMOLO_ROBOT_ID Not added"
        exit
    fi
    sudo sed "${Location}cQOMOLO_ROBOT_ID=${project}1" .env

}

# start_container
function start_container()
{
    local version=$1
    local project=$2
    local device=$3
    local trailer=$4

    adjust_param $version $project

    if [[ ! -d /opt/qomolo/utils/qpilot_setup/$version/ ]];then
        echo "version dir is not exist"
        exit
    fi
    cd /opt/qomolo/utils/qpilot_setup/$version/ && bash start_container.sh
}

function main()
{
    case "$VERSION:$PROJECT:$DEVICE:$TRAILER" in
    # v0.8
    0.8:tj:1:)
        start_container $VERSION $PROJECT $DEVICE
    ;;
    0.8:tj:2:);;
    0.8:ck::);;
    0.8:wh::);;
    0.8:dl::);;
    0.8:qp:1:);;
    0.8:qp:2:);;
    0.8:hr|xm::);;
    0.8:jk:1:on);;
    0.8:jk:1:off);;
    0.8:jk:2:on);;
    0.8:jk:2:off);;
    0.8:jj:1:on);;
    0.8:jj:1:off);;
    0.8:jj:2:on);;
    0.8:jj:2:off);;
    # v2.6
    2.6:tj:1:);;
    2.6:tj:2:);;
    2.6:ck::);;
    2.6:wh::);;
    2.6:dl::);;
    2.6:qp:1:);;
    2.6:qp:2:);;
    2.6:hr|xm::);;
    2.6:jk:1:on);;
    2.6:jk:1:off);;
    2.6:jk:2:on);;
    2.6:jk:2:off);;
    2.6:jj:1:on);;
    2.6:jj:1:off);;
    2.6:jj:2:on);;
    2.6:jj:2:off);;
    # v2.9
    2.9:tj:1:);;
    2.9:tj:2:);;
    2.9:ck::);;
    2.9:wh::);;
    2.9:dl::);;
    2.9:qp:1:);;
    2.9:qp:2:);;
    2.9:hr|xm::);;
    2.9:jk:1:on);;
    2.9:jk:1:off);;
    2.9:jk:2:on);;
    2.9:jk:2:off);;
    2.9:jj:1:on);;
    2.9:jj:1:off);;
    2.9:jj:2:on);;
    2.9:jj:2:off);;
    # v2.10
    2.10:tj:1:);;
    2.10:tj:2:);;
    2.10:ck::);;
    2.10:wh::);;
    2.10:dl::);;
    2.10:qp:1:);;
    2.10:qp:2:);;
    2.10:hr|xm::);;
    2.10:jk:1:on);;
    2.10:jk:1:off);;
    2.10:jk:2:on);;
    2.10:jk:2:off);;
    2.10:jj:1:on);;
    2.10:jj:1:off);;
    2.10:jj:2:on);;
    2.10:jj:2:off);;
    esac
}

main()