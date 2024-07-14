#!/bin/bash

readonly CONFIG=".env"

echo "调整ws配置文件"
echo "请和研发人员确定release版本"
read -p "2.10以下请输入2.9;2.10以上请输入2.10: " select

case ${select} in     
2.9)
    if [[ $(cat ${CONFIG} | grep 2.9) == "" ]];then 
        sudo sed -i "s/2.10/2.9/g" ./${CONFIG}
    fi
;;
2.10)
    if [[ $(cat ${CONFIG} | grep 2.10) == "" ]];then 
        sudo sed -i "s/2.9/2.10/g" ./${CONFIG}
    fi
;;
*)
	echo "input error. please again"
;;
esac  