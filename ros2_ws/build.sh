#!/bin/bash


source /opt/ros/foxy/setup.bash

if [[ $1 == "" ]];then
	rm -rf build install log && colcon build 
else 
	rm -rf build install log && colcon build --packages-select $1 
fi
