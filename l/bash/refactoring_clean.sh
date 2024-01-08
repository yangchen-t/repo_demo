#!/bin/bash

readonly DELETE_NUMBER=10
readonly THRESHOLD=200
readonly TMP_FILE="/tmp/clean_list.txt"
readonly SORT_TMP_FILE="/tmp/sort_clean_list.txt"
readonly DELETE_LIST=(
    "/data/code/all_ws/ws/csv"
    "/data/code/all_ws/ws/qlog/"
    "/data/code/all_ws/ws/igv_log/"
    "/data/code/all_ws/ws/coredump/"
    "/data/key_log/"
    "/data/code/all_ws/ws/logpush_nas/"
    "/data/code/all_ws/ws/qfile/"
    "/data/code/all_ws/ws/logpush_tmp/"
)
# stat
function TimeAndFilenameHandle()
{
    local time=$(stat $1 | grep Access | tail -n 1 | awk '{print$2" "$3}' 2>/dev/null)
    echo ${time}" "$1 >> ${TMP_FILE}
}

function CleanOldTimeReleaseSpace()
{
    cat ${SORT_TMP_FILE} | head -n ${DELETE_NUMBER} | awk '{print$3}' | xargs -I {} rm -v {}
    sed -i "1,${DELETE_NUMBER}d" ${SORT_TMP_FILE}
}

function ReleaseSpaceHandle()
{
    for i in "${DELETE_LIST[@]}";do
        for file in $(find ${i} -type f);do  # -maxdepth 4 
            TimeAndFilenameHandle ${file}
        done 
    done
}

while true ;do
    echo nvidia | sudo -S chown -R nvidia.nvidia /data/code/all_ws/ws/ /data/key_log 
    sleep 1
    disk_use=$(df -h | grep /data | grep -v docker | awk '{print $4}' | cut -f 1 -d "G")
    if [[ "${disk_use}" -lt "${THRESHOLD}" ]]; then
        echo "Avail ${disk_use}, will clean"
	    ReleaseSpaceHandle
        sort -n ${TMP_FILE} > ${SORT_TMP_FILE}
	    while true; do
            sleep 1; 
            CleanOldTimeReleaseSpace
            disk_use=$(df -h | grep /data | grep -v docker | awk '{print $4}' | cut -f 1 -d "G")
            if [[ "${disk_use}" -gt "${THRESHOLD}" ]]; then
                rm -r ${TMP_FILE} ${SORT_TMP_FILE}
                break  
            fi
        done 
    else
        echo ${disk_use}
    fi
done