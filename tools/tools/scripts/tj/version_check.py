#!/usr/bin/env python3 

import paramiko
import subprocess
import datetime
import time,csv
import subprocess

igv_id = range(1,7)
#igv_id = [1,24]
port = 22 
username = "nvidia"
passwd = "nvidia"
command = "dpkg -l  | grep qpilot"


subprocess.getoutput("echo "" > ~/version.csv")

print("查询时间:",datetime.datetime.now())
print("正在查询所有单车版本号----")
for ID in igv_id:
        try:
            hostname=str('10.159.'+ str(ID) +'.105')
            hostname_106=str('10.159.'+ str(ID) +'.106')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname,port,username,passwd)
            stdin,stdout,stderr = ssh.exec_command(command)
            ssh.connect(hostname,port,username,passwd)
            stdin,stdout,stderr = ssh.exec_command(command)
            f = open ("/home/qomolo/version.csv","a")
            csv_write = csv.writer(f)
            csv_write.writerow([hostname,"--" * 10 ])
            for data in stdout.readlines():
                qpilot,version =  data.split(" ")[2],data[47:85]
                csv_write.writerow([qpilot,version])
            time.sleep(1)
            ssh.close()

        except:
            print(hostname)
            print('It seems that the device cannot be connected ~')
print("查询结果保存至/home/qomolo/version.csv里")
print("---------> 打印 <------------")
subprocess.getoutput("cat /home/qomolo/version.csv")
            
