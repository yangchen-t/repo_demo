#!/bin/bash

echo "" > ~/tools/csv/speed_result.csv

echo "正在查询所有车辆速度，请稍等...."  

python3 ~/tools/scripts/speed_check.py > ~/tools/csv/speed_result.csv && cat ~/tools/csv/speed_result.csv | grep -E "line_speed|curve_speed|lane_change_speed" -B1  --color=auto

