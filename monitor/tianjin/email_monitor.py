#!/usr/bin/env python3 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import subprocess
import paramiko
import time
import csv


pt = 22 
un = pswd = "nvidia"
cmd = "dpkg -l  | grep qpilot"
emaill_str = '2876355007@qq.com'
IGV_LIST= [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]

subprocess.getoutput("echo "" > /home/qomolo/top_monitor.csv")

def sendReport():
    #发送邮箱
    # sender = '2876355007@qq.com'
    #接收邮箱
    # receiver = '2876355007@qq.com'
    #发送邮件主题
    subject = '天津定时检测系统资源报告'
    #发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    #发送邮箱用户/密码
    # username = '2876355007@qq.com'
    password = 'dpfxwudqdpesdfah'  #授权码
    #中文需参数‘utf-8’，单字节字符不需要
    #编写HTML类型的邮件正文
    test = subprocess.getoutput("cat /home/qomolo/top_report.csv")
    msg = MIMEText(test)
    #主题固定属性
    msg['Subject'] = Header(subject, 'utf-8')
    #发送者        # 接受者
    msg['from'] = msg['to'] = emaill_str
    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(emaill_str, password)
    smtp.sendmail(emaill_str, emaill_str, msg.as_string())
    smtp.quit()
    return 0

def igv_check_105(ID):
    try:
        hostname=str('10.159.'+ str(ID) +'.105')
        print(hostname)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=hostname,port=pt,username=un,password=pswd)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        f = open ("/home/qomolo/top_monitor.csv","a")
        csv_write = csv.writer(f)
        csv_write.writerow([hostname,"--" * 10 ])
        for data in stdout.readlines():
            qpilot,version =  data.split(" ")[2],data[47:85]
            csv_write.writerow([qpilot,version])
        time.sleep(1)
        ssh.close()
        return 0
    except:
        print("igv ({0}) not start ". format(hostname))
        return 0

def main():
    for ID in IGV_LIST:
        igv_check_105(ID)


if __name__ == "__main__":
    main()
    sendReport()
# print("==" * 10 +">"+"print search result"+"<"+ "==" * 10)

