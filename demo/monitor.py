#!/usr/bin/env python3 

import os
import paramiko
import sys
import time as t
import logging
import hashlib
import datetime
import subprocess


log_path_dir = "/key_log/key_log"
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

def create_folder(QOMOLO_ROBOT_ID, sftp):
#     GET_TIME = str(subprocess.getoutput("date +%Y_%m_%d"))
#     YEAR,MONTH,DAY = GET_TIME[0:4],GET_TIME[5:7],GET_TIME[8:10]
    YEAR = str(datetime.datetime.now().year)
    MONTH = str(datetime.datetime.now().month).zfill(2)
    DAY = str(datetime.datetime.now().day).zfill(2)
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
                    filename='upload.log',
                    filemode='a',##模式，有w和a，w就是写模式，每次都会重新写日志，覆盖之前的日志
                    #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '%(asctime)s-%(levelname)s: %(message)s'
                    #日志格式
                    )


def new_sftp_obj():
    for i in range(10):
        try:
            transport = paramiko.Transport(HOST, PORT)
            transport.connect(username=USERNAME, password=PASSWORD)
            sftp = paramiko.SFTPClient.from_transport(transport)
            logging.info("new sftp success")
            return sftp
        except Exception as e:
            logging.info("sftp connect error:{}".format(e))
            logging.info("retry connect.....")
            t.sleep(2)
    return None


def check_diff_process(current, new_dir_list):
    if len(current) < len(new_dir_list):
        diff = set(new_dir_list).difference(set(current))
        logging.info("have diff")
        for file in diff:
            logging.info("file:  {}".format(file))
            QOMOLO_ROBOT_ID = file.split("_")[0] + "_" + file.split("_")[1] + "_" + file.split("_")[2]
            sftp_obj = new_sftp_obj()
            if sftp_obj:
                DAY_PATH = create_folder(QOMOLO_ROBOT_ID, sftp_obj)
                file_path = os.path.join(log_path_dir, file)
                remote_path = os.path.join(DAY_PATH + "/" + QOMOLO_ROBOT_ID, file)
                t.sleep(1)
                logging.info("file_path : {}".format(file_path))
                logging.info("remote_path : {}".format(remote_path))
                logging.info("upload...")
                for i in range(10):
                    try:
                        sftp_obj.put(file_path, remote_path)
                        break
                    except Exception as e:
                        del sftp_obj
                        sftp_obj = new_sftp_obj()
                        logging.info("sftp put error!!  retry")
                logging.info(file_path + "\033[1;31;36m has been success to upload \033[0m" + remote_path)
                sftp_obj.close()
                logging.info("close sftp connect")
                return True
            else:
                logging.error("sftp obj new error")
                return False

    else:
        return False


if __name__ == '__main__':
    while True:
        current = sorted(os.listdir("/key_log/key_log"), key=str.lower)
        t.sleep(10)
        while True:
            try:
                new_dir_list = sorted(os.listdir("/key_log/key_log"), key=str.lower)
                if check_diff_process(current, new_dir_list):
                    break
                else:
                    logging.info("no diff")
                    break
            except Exception as e:
                logging.error("sftp service error:{}".format(e))
                t.sleep(5)
                break

