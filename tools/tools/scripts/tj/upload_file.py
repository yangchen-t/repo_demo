#!/usr/bin/python3

import paramiko
import os, sys
import time

servicePath = '/data/code/all_ws/ws/'

vehicle_ip = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]

def methods_select():
    method = int(input("all or one (1 or 2) : "))
    if method == int(1):
        for i in vehicle_ip:
            ip = "10.159." + str(i) + ".105"
            file_transfer(ip,sys.argv[1])
    elif method == int(2):
        for i in str(input("请输入单车序号:")).split():
            ip = "10.159."+str(i)+".105"
            file_transfer(ip,sys.argv[1])
    else :
        print("unkonw method")

def file_transfer(ip,file_name):
    port = 22
    username = password = 'nvidia'
    t = paramiko.Transport(ip,port)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.put(file_name,os.path.join(servicePath, sys.argv[1]))
    t.close()

def file_downloads(file_name):
    igv_number = str(input("请输入单车序号:"))
    local_path = str(input("存放的绝对路径"))
    ip = "10.159." +  igv_number  + ".105" 
    port = 22
    username = password = 'nvidia'
    t = paramiko.Transport(ip,port)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)
    sftp.get(file_name,local_path)
    t.close()


def timer():
    start_time  = time.time()
    if int(sys.argv[2]) == int(1):
        methods_select()
    elif int(sys.argv[2]) == int(2):
        file_downloads(sys.argv[1])
    print(time.time() - start_time)


if __name__ == '__main__':
    if len(sys.argv) < 3:
         raise SystemExit('upload or downloads (1 or 2) :')
    elif len(sys.argv) < 2:
        raise SystemExit('missing parameters')
    timer() 
