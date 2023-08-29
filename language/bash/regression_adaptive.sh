#!/bin/bash

VERSION=$1
PROJECT=$2
DEVICE=$3
TRAILER=$4
PARAM1=''
PARAM2=''
PARAM3=''
PARAM4=''

function usage() {
    echo "Template: $0 0.8 tj 1 off"
    exit
}

# check  current premission
if [ "$(id -u)" -eq 0 ]; then
    echo "Please DO NOT run the build script as root"
    exit
fi

if [[ $VERSION == "-h" ]]; then
    usage
fi

function replace_conf() {
    local version=$1
    local supervisorconf=$2

    if [[ ! -f /opt/qomolo/utils/qpilot_setup/$version/conf/${supervisorconf}.conf ]]; then
        echo "supervisorconf not exist"
        exit
    fi
    cd /opt/qomolo/utils/qpilot_setup/$version/
    Location=$(cat -n .env | grep "SUPER" | awk '{print$1}')
    if [[ $Location == "" ]]; then
        echo "SUPRE Not added"
        exit
    fi
    sudo sed -ie "${Location}cSUPER=${supervisorconf}.conf" .env
}

function modify_conf() {
    local version=$1
    local project=$2
    local device=$3
    local trailer=$4

    if [[ ! -d /opt/qomolo/utils/qpilot_setup/$version/ ]]; then
        echo "version dir is not exist"
        exit
    fi
    if [[ ! -f /opt/qomolo/utils/qpilot_setup/$version/.env ]]; then
        echo ".env file is not exist"
        exit
    fi

    cd /opt/qomolo/utils/qpilot_setup/$version/
    Location=$(cat -n .env | grep "QOMOLO_ROBOT_ID" | awk '{print$1}')
    if [[ $Location == "" ]]; then
        echo "QOMOLO_ROBOT_ID Not added"
        exit
    fi
    sudo sed -i "${Location}cQOMOLO_ROBOT_ID=${project}1" .env

    case $version:$project:$device in
    2.9:tj:1)
        replace_conf $version tj_supervisor_2.9
        ;;
    2.9:tj:2)
        replace_conf $version tj_supervisor_105_2.9/tj_supervisor_106_2.9
        ;;
    2.9:ck:1)
        replace_conf $version ceke_supervisor_2.9
        ;;
    2.9:wh:2)
        replace_conf $version wh_supervisor_105_2.9/wh_supervisor_106_2.9
        ;;
    2.9:dl:2)
        replace_conf $version dl_supervisor_105_2.9/dl_supervisor_106_2.9
        ;;
    2.9:eh:1)
        replace_conf $version eh_supervisor_2.9
        ;;
    2.9:qp:2)
        replace_conf $version Q_qp_supervisor_105_2.9/Q_qp_supervisor_106_2.9
        ;;
    2.9:qp:1)
        replace_conf $version B_qp_supervisor_105.2.9/B_qp_supervisor_106.2.9
        ;;
    2.9:xm:2)
        replace_conf $version xm_supervisor_105_2.9/xm_supervisor_106.2.9
        ;;
    2.9:jk:2)
        replace_conf $version Q_jk_supervisor_105_2.9/Q_jk_supervisor_106_2.9
        ;;
    2.9:jk:1)
        replace_conf $version jk_supervisor_105_2.9/jk_supervisor_106_2.9
        ;;
    2.9:jj:2)
        replace_conf $version T_jj_supervisor_105_2.9/T_jj_supervisor_106_2.9
        ;;
    2.9:jj:1)
        replace_conf $version T_jj_supervisor_2.9
        ;;
    esac
}

function adjust_param() {
    local version=$1
    local project=$2
    local device=$3
    local trailer=$4

    case $project in
    tj* | tianjin)
        modify_conf $version tj $device $trailer
        ;;
    ck* | ceke)
        modify_conf $version ck $device $trailer
        ;;
    eh*)
        modify_conf $version eh $device $trailer
        ;;
    wh* | wuhan)
        modify_conf $version wh $device $trailer
        ;;
    dl* | dalian)
        modify_conf $version dl $device $trailer
        ;;
    qp* | qingpu)
        modify_conf $version qp $device $trailer
        ;;
    hr* | xm* | xiamen)
        modify_conf $version hr $device $trailer
        ;;
    jk* | jinke)
        modify_conf $version jk $device $trailer
        ;;
    jj* | jingjiang)
        modify_conf $version jj $device $trailer
        ;;
    esac
}

# start_container
function start_container() {
    local version=$1
    local project=$2
    local device=$3
    local trailer=$4

    adjust_param $version $project $device $trailer

    if [[ ! -d /opt/qomolo/utils/qpilot_setup/$version/ ]]; then
        echo "version dir is not exist"
        exit
    fi
    cd /opt/qomolo/utils/qpilot_setup/$version/ &&
        echo "============check_config============" &&
        cat .env &&
        echo "====================================" &&
        sleep 1 &&
        bash start_container.sh &&
        docker exec -it qpilot bash
}

function main() {
    start_container $VERSION $PROJECT $DEVICE $TRAILER
}
main
