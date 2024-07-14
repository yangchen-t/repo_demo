#!/bin/bash

fstab="/etc/fstab"
readonly mountPoint="/data"
readonly choose=$1
readonly disk="/dev/nvme0n1p1"
readonly status_log="/tmp/disk_status"
readonly sign="/home/$(logname)/.sign"

Usages()
{
    echo "Usage: $0 [option]"
    echo "Options:"
    echo "-s     : 移除自动挂载"
    echo "-r     : 恢复自动挂载"
    echo "-m     : 手动挂载为只读文件系统"
    echo "-mr    : 手动移除挂载的只读文件系统"
    echo "-i     : 查看当前状态"
    exit -1
}

setFstab()
{
    if [ $(cat ${sign}) == "-s" ];then
        echo "already set fstab, Do not repeat the settings"; return -1
    fi
    sudo sed -i "${1} s/^/#/" ${fstab}
    echo "[${FUNCNAME}] set fstab finish" | sudo tee ${status_log}
}

resetFstab()
{
    sudo sed -i "${1} s/^#//" ${fstab}
    echo "[${FUNCNAME}] reset fstab finish"  | sudo tee ${status_log}
}

mountReadOnlyFileSystem()
{
    sudo mount -o ro ${disk} /data/ 
    echo "[${FUNCNAME}] set disk read-only finish" | sudo tee ${status_log}
}

umountReadOnlyFileSystem()
{
    sudo umount /data/ 
    echo "[${FUNCNAME}] umount disk finish" | sudo tee ${status_log}
}

infoCurrentStatus()
{
    if [ ! -f ${sign} ];then
        echo "null"; return 0
    fi
    echo "$(cat ${status_log}) " "-> sign:" " $(cat ${sign})"
}

main()
{
    local number=$(cat /etc/fstab | grep "/data" -n  | awk -F ":" '{print$1}')
    case ${choose} in
    "-s")
        setFstab ${number} ;;
    "-r")
        resetFstab ${number} ;;
    "-m")
        mountReadOnlyFileSystem ;;
    "-mr")
        umountReadOnlyFileSystem ;;
    "-i")
        infoCurrentStatus ;;
    *)
        Usages ;;
    esac
    sudo echo ${choose} > ${sign}
}

main 