#!/bin/bash


echo "" > ~/tools/csv/version_result.csv


echo "正在查询所有车辆版本，请稍等...."
python3 ~/tools/scripts/version_check.py > ~/tools/csv/version_result.csv && cat ~/tools/csv/version_result.csv | grep "qpilot" -B1 --color=auto

