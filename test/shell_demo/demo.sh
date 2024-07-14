#!/bin/bash

# set -x 

# 原始字符串
original_string="[program:control]
command=/scripts/%(program_name)s.sh
stdout_logfile=/debug/%(program_name)s.log
stdout_logfile_maxbytes=10MB
stdout_logfile_backups=50
redirect_stderr=true
autostart=false
autorestart=true
stopasgroup=true
stopsignal=INT"

# 要添加的内容
start="autostart=true"
restart="autorestart=false"

# 要添加到哪里
insert_point="redirect_stderr=true"

test1()
{
    local _tmp="1"
    test2
}
test2()
{
    echo ${_tmp}
}

test2
autostart=$(echo ${original_string} | grep -oP "autostart=\K\w+" || echo "${start}")

# # 检查是否存在要添加的位置
# if [[ "$original_string" == *"$insert_point"* ]]; then
#     if [[ "$original_string" == *"autostart"* ]];then
#         original_string=$(echo "$original_string" | sed -E "s/autostart=.*/$start/")
#     else 
#         original_string=$(echo "$original_string" | sed -E "s/$insert_point/$insert_point\n$start/")
#     fi 
#     if [[ "$original_string" = *"autorestart"* ]];then
#         original_string=$(echo "$original_string" | sed -E "s/autorestart=.*/$restart/")
#     else 
#         original_string=$(echo "$original_string" | sed -E "s/$insert_point/$insert_point\n$restart/")
#     fi 
#     echo "$original_string"
# else
#     echo "456"
# fi
echo ${autostart}