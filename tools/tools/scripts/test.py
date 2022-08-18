#!/usr/bin/env python3

import paramiko
import threading
import time

port = 22
username = "nvidia"
passwd = "nvidia"

class IgvVehicleTools():
        def __init__(self) -> None:
                pass

        def sshclient_execmd(self,hostname, port, username, password, execmd):
                try:
                        s = paramiko.SSHClient()
                        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        s.connect(hostname=hostname, port=port, username=username, password=password)
                        stdin, stdout, stderr = s.exec_command(execmd,timeout=5)
                        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
                        print(stdout.read().decode())
                        s.close()
                except:
                        print(hostname,"---> " + "finish")

        def qpilot_config(self):

                #qpilot,param =  input("qpilot版本：").split(" ")[-1],input("参数版本：").split(" ")[-1]
                #print(qpilot)
                #print(param)
                #cmd = 'echo nvidia | sudo -S apt update ; yes | sudo apt install qomolo-gcs-scripts'
                cmd = 'igv_passwd xiangyang.chen && echo nvidia | sudo -S apt update && yes | sudo apt install qpilot={0} qpilot-param={1}' .format(qpilot,param)
                #cmd_reboot = [ "echo nvidia | sudo -S apt update && yes | sudo apt install qpilot={0} qpilot-param={1} && \
                #bash /opt/qomolo/utils/qpilot_setup/all_supervisord/start_container.sh" .format(qpilot,param)]   #带重启
                cmd_mode = input("是否需要重启车辆 （y/n）：")
                igv_ip = int(input("操作全部车辆(0)/还是单个车辆(1)："))
                if igv_ip == int(0) :
                    igv_list = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]
                    for i in igv_list :
                            ip = str("10.159."+str(i)+".105")
                            if cmd_mode == "n":
                                    self.sshclient_execmd(ip, port, username, passwd, cmd)      
                            elif cmd_mode == "y":
                                    self.sshclient_execmd(ip, port, username, passwd, cmd_reboot)
                            else:
                                    print("please input y / n ！！")

                elif igv_ip == int(1):
                        igv_list = str(input("请输入单车序号:")).split()
                        for i in igv_list:
                                ip = str("10.159."+str(i)+".105")
                                print(ip)
                                if cmd_mode == "n":
                                        self.sshclient_execmd(ip, port, username, passwd, cmd)
                                elif cmd_mode == "y":
                                        self.sshclient_execmd(ip, port, username, passwd, cmd_reboot)
                                else:
                                        print("please input y / n ！！")
                else:
                        print("please input number 0 or 1 !!")
   


if __name__ == "__main__" :
    print("这是一个版本升级工具")
    igv = IgvVehicleTools()
    igv.qpilot_config()

