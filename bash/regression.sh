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

    case $project in
    tj*|tianjin)
        modify_env $version tj
    ;;
    ck*|ceke)
        modify_env $version ck
    ;;
    wh*|wuhan)
        modify_env $version wh
    ;;
    dl*|dalian)
        modify_env $version dl
    ;;
    qp*|qingpu)
        modify_env $version qp
    ;;
    hr*|xm*|xiamen)
        modify_env $version hr
    ;;
    jk*|jinke)
        modify_env $version jk
    ;;
    jj*|jingjiang)
        modify_env $version jj
    ;;
    esac 
}

function modify_env()
{
    local version=$1
    local project=$2
    if [[ ! -d /opt/qomolo/utils/qpilot_setup/$version/ ]];then
        echo "version dir is not exist"
        exit
    fi
    if [[ ! -f /opt/qomolo/utils/qpilot_setup/$version/.env ]];then
        echo ".env file is not exist"
        exit
    fi 

    sudo sed -i 's/QOMOLO_ROBOT_ID=' # TODO  sed select replace
}

# start_container
function start_container()
{
    local version=$1
    local project=$2
    local device=$3
    local trailer=$4


}


case "$VERSION:$PROJECT:$DEVICE:$TRAILER" in
)
;;
esac