#!/bin/bash

#echo "" > ~/tools/csv/update_result.csv

echo "正在启动版本控制程序，请稍等...."  

python3 ~/tools/scripts/update_check.py 
#> ~/tools/csv/update_result.csv && cat ~/tools/csv/update_result.csv | grep "update-finish" -B1  --color=auto

