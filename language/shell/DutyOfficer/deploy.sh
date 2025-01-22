#!/bin/bash

opts1=${1}
opts2=${2}
declare -g  COVER=

lib_dir="/lib/systemd/system/"

enable()
{
    sudo systemctl enable ${1}
    sudo systemctl start ${1}
}

disable()
{
    sudo systemctl stop ${1}
    sudo systemctl disable ${1}
}

main()
{
    for i in $(ls ./service | grep service$);do
        case ${COVER} in
        "true")
            sudo cp -v ./service/${i} ${lib_dir}
            enable ${i}
            ;;
        *)
            if [ ! -f ${lib_dir}/${i} ];then
                sudo cp ./service/${i} ${lib_dir}
                enable ${i}
            fi
        ;;
        esac
    done
}

case "${opts1}:${opts2}" in 
"enable":)
    main ;;
"enable":"-f")
    COVER="true"
    main ;;
"disable":)
    for i in $(ls ./service | grep service$);do
        disable ${i}
    done ;;
*:*)
    echo "options <enable/disable/-h>"
esac