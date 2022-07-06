#!/usr/bin/env python3 


#兼容不同固件升级，不同车辆升级，一键升级，信息查询，
############

import paramiko

igv_list = [1,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]
port = 22
username = "nvidia"
passwd = "nvidia"
check_version = "dpkg -l  | grep qpilot"

class IgvVehicleTools():

    def __init__(self) -> None:
        pass

    def qpilot_config():

        name = input("固件名称：")
        version = input("固件版本：")

        cmd = 'echo nvidia | sudo -S apt update && yes | sudo apt install $s=%s' % name,version
        cmd_reboot = ['echo nvidia | sudo -S apt update && yes | sudo apt install $s=%s &&  \
                       bash /opt/qomolo/utils/qpilot_setup/all_supervisord/start_container.sh' % name version]   #带重启
        igv_ip = int(input("操作全部车辆(0)/还是单个车辆(1)：")）
        if igv_ip == int(0) :
            cmd_mode = input("是否需要重启车辆 （y/n）：")
            for i in igv_list:
                ip = str("10.159."+str(i)+".105")

        elif igv_ip == int(1):
            igv_list = str(input("请输入单车序号:")).split()
            for i in igv_list:
                ip = str("10.159."+str(i)+".105")
        else:
            print("please input number 0 or 1 !!")
        if cmd_mode == "n":
            sshclient_execmd(hostname=ip ,port=port, username=username, password=passwd , execmd=cmd)
        elif cmd_mode == "y":
             sshclient_execmd(hostname=ip ,port=port, username=username, password=passwd , execmd=cmd_reboot)
        else :
            print("please input y / n ！！")

    def igv_check_version():
            for ID in igv_list:
                hostname=str('10.159.'+ str(ID) +'.105')
                print(hostname,"---> ---> ---> --->")
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(hostname,port,username,passwd)
                stdin,stdout,stderr = ssh.exec_command(check_version)
                for data in stdout.readlines():
                    print(data)
                    ssh.close()
   
    def sshclient_execmd(hostname, port, username, password, execmd):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd,timeout=2)
        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
        print(stdout.read().decode())
        s.close()





if __name__ == "__main__" :
    print("""
    选择想要进行的操作：
    升级固件版本 -> 1 :
    查看车辆信息(.env) -> 2 :
    查询当前车辆上的版本信息 -> 3 :
    """)
    number = int(input(":"))
    if number == int(1) :





