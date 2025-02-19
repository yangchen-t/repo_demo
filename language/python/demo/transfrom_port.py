#!/usr/bin/env python3 

import paramiko
import base64
import sys


key = b'Z2F0ZUB3ZXN0Iw=='
port = 22
username = "qomolo"
passwd = base64.b64decode(key).decode()          #base64        


def transfrom_func(sim_ip,vehicle_ip,type_operation="A"):
    try:
        cmd = "echo  {0} | sudo -S iptables -t nat -{2} PREROUTING -p tcp --dport 4000 -j DNAT --to-destination {1}:4000".format(
                passwd, vehicle_ip, type_operation)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(sim_ip,port,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        ssh.close()
    except:
        print('ERROR',sim_ip)

def Doc_func():
        print('''
        需要添加参数：
        python3 transfrom_port.py 4Gip / 车辆ip / (AorD)
        ''')

def main():
    if len(sys.argv) == 4:
        transfrom_func(sys.argv[1], sys.argv[2],sys.argv[3])
        print("finish")
    elif len(sys.argv) == 3:
        transfrom_func(sys.argv[1], sys.argv[2])
        print("finish")
    else:
        print("command not unknow.")
        Doc_func()
        

if __name__ == "__main__":
    main()
    


