#!/usr/bin/env python3 


import paramiko


igv_id = [21,22,23,24,25,26,27,28,29,30,31,32,33,73,76]
port = 22 
username = "nvidia"
passwd = "nvidia"
command = "dpkg -l  | grep qpilot"

print("正在查询所有单车版本号----")
for ID in igv_id:
        try:
            hostname=str('10.159.'+ str(ID) +'.105')
            print(hostname,"---> ---> ---> --->")
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname,port,username,passwd)
            stdin,stdout,stderr = ssh.exec_command(command)
            for data in stdout.readlines():
                print(data)
            ssh.close()
        except:
            print('It seems that the device cannot be connected ~~')

