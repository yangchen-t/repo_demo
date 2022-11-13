#!/usr/bin/python3

import paramiko
import os, sys
import time

servicePath = '/data/code/all_ws/ws/'

vehicle_ip = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]

def file_transfer(ip,file_name):
    port = 22
    username = password = 'nvidia'
    t = paramiko.Transport(ip,port)
    t.connect(username=username, password=password)
    sftp = paramiko.SFTPClient.from_transport(t)

    sftp.put(file_name,os.path.join(servicePath, sys.argv[1]))
    t.close()

def timer():
    for i in vehicle_ip:
        ip = "10.159." + str(i) + ".105"
        start_time  = time.time()
        file_transfer(ip,sys.argv[1])
        print(time.time() - start_time)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        raise SystemExit('missing parameters')
    timer() 