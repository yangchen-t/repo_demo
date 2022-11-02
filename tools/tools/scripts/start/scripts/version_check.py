#!/usr/bin/env python3

import subprocess
import paramiko
import time
import csv



pt = 22 
un = "nvidia"
pswd = "nvidia"
cmd = "dpkg -l  | grep qpilot"

subprocess.getoutput("echo "" > /home/qomolo/version.csv")
def igv_check_105(ID):
    try:
            hostname=str('10.159.'+ str(ID) +'.105')
            print(hostname)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname,port=pt,username=un,password=pswd)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            f = open ("/home/qomolo/version.csv","a")
            csv_write = csv.writer(f)
            csv_write.writerow([hostname,"--" * 10 ])
            for data in stdout.readlines():
                  qpilot,version =  data.split(" ")[2],data[47:85]
                  csv_write.writerow([qpilot,version])
            time.sleep(1)
            ssh.close()
    except:
            print("igv ({0}) not start ". format(hostname))
def igv_check_106(ID):
      try:
            hostname=str('10.159.'+ str(ID) +'.106')
            print(hostname)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=hostname,port=pt,username=un,password=pswd)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            f = open ("/home/qomolo/version.csv","a")
            csv_write = csv.writer(f)
            csv_write.writerow([hostname,"--" * 10 ])
            for data in stdout.readlines():
                  qpilot,version =  data.split(" ")[2],data[47:85]
                  csv_write.writerow([qpilot,version])
            time.sleep(1)
            ssh.close()
      except:
            print("igv ({0}) not start ". format(hostname))
if __name__ == "__main__":
      for ID in range(1,7):
            igv_check_105(ID)
            igv_check_106(ID)
print("==" * 10 +">"+"print search result"+"<"+ "==" * 10)
print(subprocess.getoutput("cat /home/qomolo/version.csv"))

