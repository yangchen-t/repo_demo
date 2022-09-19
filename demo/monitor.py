#!/usr/bin/env python3 

import os
import paramiko
import sys
import time as t
import logging
import hashlib
import datetime


log_path_dir = "/data/code/all_ws/ws/logpush_nas"
HOST = "192.168.103.77"
PORT = 22
USERNAME = "xiangyang.chen"
PASSWORD = "AAxijing123.."
ROOT_PATH = "/data/qpilot_log/igv"

def get_md5(filename):
    if os.path.isfile(filename):
        with open(filename,'rb') as fp:
            data = fp.read()
            return hashlib.md5(data).digest()
    else:
        logging.info("no file " + filename)

def create_folder(QOMOLO_ROBOT_ID):
    YEAR = str(datetime.datetime.now().year)
    MONTH = str(datetime.datetime.now().month)
    DAY = str(datetime.datetime.now().day)
    YEAR_PATH = ROOT_PATH + "/" + YEAR
    MONTH_PATH = YEAR_PATH + "/" + MONTH
    DAY_PATH = MONTH_PATH + "/" + DAY
    ID_PATH = DAY_PATH + "/" + QOMOLO_ROBOT_ID
    year_existence = True if YEAR in sftp.listdir(ROOT_PATH) else False
    if not year_existence:
        sftp.mkdir(YEAR_PATH)
    month_existence = True if MONTH in sftp.listdir(YEAR_PATH) else False
    if not month_existence:
        sftp.mkdir(MONTH_PATH)
    day_existence = True if DAY in sftp.listdir(MONTH_PATH) else False
    if not day_existence:
        sftp.mkdir(DAY_PATH)
    id_existence = True if QOMOLO_ROBOT_ID in sftp.listdir(DAY_PATH) else False
    if not id_existence:
        sftp.mkdir(ID_PATH)
        logging.info("create "+ ID_PATH)
    return DAY_PATH

logging.basicConfig(level=logging.INFO,#控制台打印的日志级别
                    filename='/home/nvidia/upload.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                    #日志格式
                    )
transport = paramiko.Transport(HOST, PORT)
transport.connect(username=USERNAME, password=PASSWORD)
sftp = paramiko.SFTPClient.from_transport(transport)

while True:
      current = sorted(os.listdir("/data/code/all_ws/ws/logpush_nas"),key=str.lower)
      print(current)
      print("cu")
      while True :
            t.sleep(10)
            new_dir_list = sorted(os.listdir("/data/code/all_ws/ws/logpush_nas"),key=str.lower)
            print(new_dir_list)
            print("new")
            if len(current) < len(new_dir_list):
                  diff = set(new_dir_list).difference(set(current))
                  for file in diff:
                        print(file)
                        QOMOLO_ROBOT_ID = file.split("_")[0]
                        DAY_PATH = create_folder(QOMOLO_ROBOT_ID)
                        file_path = os.path.join(log_path_dir, file)
                        remote_path = os.path.join(DAY_PATH+"/"+QOMOLO_ROBOT_ID, file)
                        t.sleep(5)
                        logging.info(remote_path)
                        logging.info(remote_path)
                        sftp.put(file_path, remote_path)
                        logging.info(file_path +"\033[1;31;36m has been success to upload \033[0m" + remote_path)
                        break
                  break
            else:
                  print("no diff")
                  break

