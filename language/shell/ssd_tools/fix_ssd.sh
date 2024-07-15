#!/bin/bash
# NOTE update_fw_v: E23907

# set -x  # debug mode
set -u  # variable check
set -e

sDependsTools="nvme"
sFwFile="fwdisk_M28_kioxia5_cmfg.fw"
sDebPath="./debs/"
sFwPath="./fw/"
sDeviceName="/dev/nvme0n1"
sSsdDownload="fw-download"
sSsdSave="fw-commit"
sSsdOldVersion="E22C23"
sSsdNewVersion="E23907"
sSsdToolsDir="ssd_tools"
sArgs1=${1:-"update"}

Logger()
{
    _RED='\033[0;31m'      # error
    _GREEN='\033[0;32m'    # INFO
    _YELLOW='\033[0;33m'   # WARN
    _NC='\033[0m'          # NORMAL
    case "${1}" in
    "E") printf "${_RED}${2}${_NC}\n";;        
    "I") printf "${_GREEN}${2}${_NC}\n";;
    "W") printf "${_YELLOW}${2}${_NC}\n";;
    *|"N") printf "${2}${_NC}\n";;
    esac
}

Usages()
{
    echo "Usage: $0 [option]"
    echo "Options:"
    echo -e "\tupdate: update fw version"
    echo -e "\tremove: remove fw tools"
}

PreCheck()
{
    which ${sDependsTools} >/dev/null 2>&1
    if [ $? -ne 0 ];then
    	sudo apt install ./debs/*.deb -y
    fi

    if ! [ -f ${sFwPath}/${sFwFile} ];then
        Logger E "file is not exist";
    fi
}

Update_Fw()
{
    # update
    time sudo ${sDependsTools} ${sSsdDownload} ${sDeviceName} -f ${sFwPath}/${sFwFile}
    time sudo ${sDependsTools} ${sSsdSave} ${sDeviceName} -s 1
    # check
    _sUpdateAfterFw=$(sudo nvme list | tail -n 1 | awk '{print$NF}')
    if [[ ${sSsdNewVersion} == ${_sUpdateAfterFw} ]];then
        Logger I "update finish"
    else
        Logger W "update failed"
    fi
}

Current_Fw()
{
    _sCurtFw=$(sudo nvme list | tail -n 1 | awk '{print$NF}')
    if [[ ${_sCurtFw} != ${sSsdOldVersion} ]];then
        Logger E "type is not supported"
        Logger N "Cur: ${_sCurtFw}"
        exit -1
    fi
}

main()
{
    case ${sArgs1} in
    "remove")
        if [[ $(basename $(pwd)) == ${sSsdToolsDir} ]];then
            { 
                cd ../ && sudo rm -r ${sSsdToolsDir}
                Logger I "delete finish"
            }
        fi
    ;;
    "update") PreCheck && Current_Fw && Update_Fw ;;
    *) Usages ;;
    esac
}
main