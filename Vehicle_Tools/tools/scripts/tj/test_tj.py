#!/usr/bin/env python3

import paramiko
import sys
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
                        stdin, stdout, stderr = s.exec_command(execmd)
                        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
                        print(stdout.read().decode())
                        s.close()
                except:
                        pass

        def qpilot_config(self,cmd):
                igv_ip = int(input("操作全部车辆(0)/还是单个车辆(1)："))
                if igv_ip == int(0) :
                    igv_list = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]
                    for i in igv_list :
                             ip = str("10.159."+str(i)+".105")
                             print(ip)
                             self.sshclient_execmd(ip, port, username, passwd, cmd)      

                elif igv_ip == int(1):
                        igv_list = str(input("请输入单车序号:")).split()
                        for i in igv_list:
                              ip = str("10.159."+str(i)+".105")
                              self.sshclient_execmd(ip, port, username, passwd, cmd)

                else:
                        print("please input number 0 or 1 !!")
   

if __name__ == "__main__" :
      print("这是一个版本升级工具")
      cmd_str = str(sys.argv[1])
      cmd = 'echo nvidia | sudo -S apt update ; sudo apt install -y {0}' .format(cmd_str)
      igv = IgvVehicleTools()
      igv.qpilot_config(cmd)
