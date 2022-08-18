#!/bin/bash

cp /scripts/pic/lib/lib* /lib
source /opt/qomolo/qpilot/setup.bash
python3 /scripts/pic/lib/led_server.py & 
while :
do
	sleep 1
	./pic/lib/led_server
done

PID=`ps -aux |grep led_server.py | awk '{print $2}'`
sudo kill -9 $PID
