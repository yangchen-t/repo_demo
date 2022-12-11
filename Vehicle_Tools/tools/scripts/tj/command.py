#!/usr/bin/env python3

import paramiko
import threading
import sys
import time

port = 22 
username = "nvidia"
passwd = "nvidia"
command = 'docker exec qpilot -c "bash data_record.sh"'



def record(hostname,port,username,passwd,command):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.close()
    except:
        print('ERROR',hostname)


def timer():
    if sys.argv[1] == "-m":
        igv_list = str(input("请输入单车序号:")).split()
        for i in igv_list:
            ip = str("10.159."+str(i)+".105")
            threading.Thread(work=record,args=(ip,port,username,passwd,command)).start()    
    else:
        ip = str("10.159."+str(sys.argv[1])+".105")
        print(ip)
        record(ip,port,username,passwd,command)



def main():
    start = time.time()
    timer()
    end = (time.time() - start)
    return end

if __name__ == "__main__":
        main()