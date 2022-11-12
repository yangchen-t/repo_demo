#!/bin/bash


git_nginx_config="}
include       fastcgi_params;
# 包涵默认的 fastcgi 参数；
fastcgi_param REMOTE_USER $remote_user;
# 将认证用户信息传递给 fastcgi 程序
fastcgi_param PATH_INFO           $1;
fastcgi_param GIT_PROJECT_ROOT    /opt;
# git 库在服务器上的跟目录
fastcgi_param GIT_HTTP_EXPORT_ALL ;
fastcgi_param SCRIPT_FILENAME /usr/lib/git-core/git-http-backend;
fastcgi_pass  unix:/var/run/fcgiwrap.socket;
# FastCGI 参数
auth_basic_user_file /etc/nginx/passwd;
# 认证的用户文件
auth_basic Restricted;
使用 Basic 认证
location ~ /git(/.*) {"


# need tools 
sudo apt update;sudo apt install git nginx fcgiwrap 

# create repo
sudo git init --bare /opt/qpilot-hw-param 
sudo chmod a+w /opt/qpilot-hw-param

# config nginx web http server 
echo $git_nginx_config | xargs -I {} sudo sed -i '52a {}' /etc/nginx/sites-available/default 
sudo nginx -s reload 

# add username and passwd 
sudo htpasswd  /etc/nginx/passwd {}      # {} 用户