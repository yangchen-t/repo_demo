#!/usr/bin/env python3 


#兼容不同固件升级，不同车辆升级
############

import paramiko
import threading

igv_list = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]
port = 22
username = "nvidia"
passwd = "nvidia"

class IgvVehicleTools():

    def __init__(self) -> None:
        pass


    def sshclient_execmd(self,hostname, port, username, password, execmd):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd,timeout=5)
        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
        print(stdout.read().decode())
        s.close()



    def qpilot_config(self):

        name = input("固件名称：")
        version = input("固件版本：")

        cmd = 'echo nvidia | sudo -S apt update && yes | sudo apt install {0}={1}' .format(name,version)
        cmd_reboot = [ "echo nvidia | sudo -S apt update && yes | sudo apt install {0}={1} && \
            bash /opt/qomolo/utils/qpilot_setup/all_supervisord/start_container.sh" .format(name,version)]   #带重启
        cmd_mode = input("是否需要重启车辆 （y/n）：")
        igv_ip = int(input("操作全部车辆(0)/还是单个车辆(1)："))
        if igv_ip == int(0) :
            for i in igv_list:
                ip = str("10.159."+str(i)+".105")
                if cmd_mode == "n":
                    sing_thread = threading.Thread(target=self.sshclient_execmd,args=(ip, port, username, passwd, cmd))
                elif cmd_mode == "y":
                    sing_thread = threading.Thread(target=self.sshclient_execmd,args=(ip, port, username, passwd, cmd))
                else:
                    print("please input y / n ！！")
                sing_thread.start()
                sing_thread.join()

        elif igv_ip == int(1):
            igv_list = str(input("请输入单车序号:")).split()
            for i in igv_list:
                ip = str("10.159."+str(i)+".105")
                if cmd_mode == "n":
                    sing_thread = threading.Thread(target=self.sshclient_execmd,args=(ip, port, username, passwd, cmd))
                elif cmd_mode == "y":
                    sing_thread = threading.Thread(target=self.sshclient_execmd,args=(ip, port, username, passwd, cmd))
                else:
                    print("please input y / n ！！")
                sing_thread.start()
                sing_thread.join()        
        else:
            print("please input number 0 or 1 !!")
   



if __name__ == "__main__" :
    print("这是一个版本升级工具")
    igv = IgvVehicleTools()
    igv.qpilot_config()




