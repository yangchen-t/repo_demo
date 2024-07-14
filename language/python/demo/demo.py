# !/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import zipfile
import shutil
import time
import datetime
import requests

csv_pdf_files = []
zip_filename =  "dl_{0}.zip".format(
     datetime.datetime.now().strftime("%Y%m%d")
)

def param():
    input_list = input("请输入开始车号 [多个车号用空格分隔]--> ").split()
    boat_id = input("请输入船名 --> ")
    start_time = input("输入开始时间，例[2022-09-15 05:20:00]--> ")
    end_time = input("输入开始时间，例[9999-12-31 13:14:00]--> ")

    if not input_list:
        print("车号err"); exit(-1) 
    if any(var == "" for var in [boat_id, start_time, end_time]):
        print("参数输入err"); exit(-1)

    data = {
        "truck_id": input_list,
        "boat_id": boat_id,
        "start_time": start_time,
        "end_time": end_time
    }
    return data


# 生成当次实船数据
def make_users(IP, data):
    url = "http://" + IP + "/WellGNS/KPI_PDF"
    response = requests.post(url=url, json=data).text
    print(response)
    print(type(response))

# 只当前路径下的所有.csv和.pdf文件
def list_csv_pdf_files_in_current_directory(current_dir):
    for file in os.listdir(current_dir):
        if file.endswith('.csv') or file.endswith('.pdf'):
            file_path = os.path.join(current_dir, file)
            csv_pdf_files.append(file_path)

# 压缩文件
def compressflie(current_dir):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in csv_pdf_files:
            print("已压缩文件：" + file)
            if os.path.exists(file):
                file_name = os.path.basename(file)
                os.chdir(current_dir)
                zipf.write(file_name)

# 移动所有符合list_csv_pdf_files_in_current_directory的文件至destination_path
def move_useless_file(destination_path):
    os.makedirs(destination_path, exist_ok=True)
    for file in csv_pdf_files:
        if os.path.exists(file):
            file_name = os.path.basename(file)
            destination_file_path = os.path.join(destination_path, file_name)
            shutil.move(file, destination_file_path)

def main():

    destination_path = "/home/qomolo/VOC/static/KPIData/tmp_data/"
    current_dir = "/home/qomolo/VOC/static/KPIData/"
    IP = "127.0.0.1:19020"
    make_users(IP, param())
    print("为确保数据生成, 休眠10s")
    time.sleep(10)
    list_csv_pdf_files_in_current_directory(current_dir)
    compressflie(current_dir)
    time.sleep(1)
    move_useless_file(destination_path)
    print("已生成压缩包：" + zip_filename + " 并将csv及pdf文件移动至:" + destination_path)

if __name__ == '__main__':
    main()
