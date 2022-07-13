#!/bin/bash


sudo systemctl stop todeskd.service
sudo mv /opt/todesk/config/todeskd.conf /opt/todesk/config/todeskd.conf.bak
sudo systemctl start todeskd.service
