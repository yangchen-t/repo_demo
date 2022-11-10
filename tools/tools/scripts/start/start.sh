#!/bin/bash


exist_images=`docker images |grep flask_web`

if [[ $exist_images == "" ]];then
	cd ./config/ && docker build flask_web_update . 
else 
	docker-compose down && docker-compose up -d 
fi 
