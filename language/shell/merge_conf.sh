#!/bin/bash

merge_conf()
{
    config=${1}
    confd="$(dirname "${config}")/conf.d/"
    run_config="/var/run/$(basename "${config}")"

    # fix permission
    sudo touch "${run_config}"
    sudo chown $(logname) "${run_config}"

    > "${run_config}"

    # sort 00 > 01
    for inc_file in $(ls -1 "${confd}" | sort); do
        if [[ -f "${confd}/${inc_file}" ]]; then
            while IFS= read -r line; do
                if [[ ! "${line}" =~ ^include\ (.*) ]]; then
                    if [[ ! "${line}" =~ ^$|^# ]]; then # ignore #&space
                        echo "${line}" >> "${run_config}"
                    fi
                fi
            done < "${confd}/${inc_file}"
        fi
    done

    # add main file
    while IFS= read -r line; do
        if [[ ! "${line}" =~ ^include\ (.*) ]]; then

            if [[ ! "${line}" =~ ^$|^# ]]; then 
                echo "${line}" >> "${run_config}"
            fi
        fi 
    done < "${config}"
    echo "${run_config}"
}


ret=$(merge_conf "/etc/myapp/myapp.conf")
cat ${ret}