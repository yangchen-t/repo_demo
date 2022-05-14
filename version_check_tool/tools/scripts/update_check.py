#!/usr/bin/env python3 


import paramiko
import threading
import time 
import os 


print("所有单车更新 or 单个单车更新 （1 or 2 ）")
number = str(input(":"))
print("输入单车序号更新指定版本")
version = str(input(":"))

command = 'echo nvidia | sudo -S apt update && yes | sudo apt install qpilot=%s' % version
#command = ['echo nvidia | sudo -S apt update && yes | sudo apt install qpilot=%s &&  \
#bash /opt/qomolo/utils/qpilot_setup/all_supervisord/start_container.sh',version]
username = "nvidia"  # 用户名
passwd = "nvidia"  # 密码 
port = 22


if number == str(1):

    print("Begin......")

    def sshclient_execmd(hostname, port, username, password, execmd):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
        print(stdout.read().decode())
        s.close()
        igv_id = [21,22,23,24,25,26,27,28,29,30,31,32,33,73,76]
        for i in igv_id:
            ip = str("10.159."+str(i)+".105")
            print("update_version =%s" % version)
            sing_thread = threading.Thread(target=sshclient_execmd,args=(ip, port, username, passwd, command))
            sing_thread.start()
            sing_thread.join()
            print("update-finish!!")

elif number == str(2):

    print("依次输入需要更新的单车")

    def sshclient_execmd(hostname, port, username, password, execmd):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
        print(stdout.read().decode())
        s.close()

    igv_id = str(input(":")).split()
    for i in igv_id:
        ip = str("10.159."+str(i)+".105")
        print("Begin......")
        print("start update %s" % version)
        sing_thread = threading.Thread(target=sshclient_execmd,args=(ip, port, username, passwd, command))
        sing_thread.start()
        sing_thread.join()
        print("update-finish!!")

else:
    print("I don't understand!!")

