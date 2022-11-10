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
                cmd = 'echo nvidia | sudo -S apt update ; sudo apt install -y {0}' .format(cmd_str)
                igv_list = range(1,9)
                for i in igv_list :
                        ip = str("10.159."+str(i)+".105")
                        print(ip)
                        self.sshclient_execmd(ip, port, username, passwd, cmd)    
                        ip = str("10.159."+str(i)+".106")  
                        print(ip)
                        self.sshclient_execmd(ip, port, username, passwd, cmd)


