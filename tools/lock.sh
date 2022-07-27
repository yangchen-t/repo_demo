#!/bin/bash

while true;do
	key=`cat ~/.env`
	if [[ $key == "xiangyang.chen" ]];then
		echo "2"
		sudo chattr -a ~/Downloads
	else
		echo "1"
		sudo chattr +a ~/Downloads
	fi
done
