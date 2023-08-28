#!/usr/bin/env python3 

import subprocess
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
import time 


HOSTNAME = subprocess.getoutput("hostname")
subprocess.getoutput("echo 'time','cpu','mem' >> /data/code/all_ws/ws/{}-SystemStat.csv".format(HOSTNAME))
class Encryption(object):

    def __init__(self) -> None:
        pass    
        
    def decrypt(self,ksa, s):
        if len(bytearray(str(s).encode("utf-8"))) % 2 != 0:
            return ""
        b = bytearray(len(bytearray(str(s).encode("utf-8"))) // 2)
        j = 0
        for i in range(0, len(bytearray(str(s).encode("utf-8"))) // 2):
            c1 = (bytearray(str(s).encode("utf-8"))[j]) - 46 
            c2 = (bytearray(str(s).encode("utf-8"))[j + 1]) -46 
            j += 2
            b[i] = (c2 * 19 + c1) ^ ksa
        return b.decode("utf-8")

class SystemStat(Encryption):

    def __init__(self) -> None:
        pass

    def timing_record(self):
        time.sleep(3)
        GET_MEM_CMD = "awk '{print $4}'  | cut -f 1 -d 'G'"
        GET_MEM_FREE = subprocess.getoutput("echo nvidia | sudo -S df -h | grep /data| grep -v docker | {0}" .format(GET_MEM_CMD))
        print(GET_MEM_FREE)
        GET_CPU_CMD = "awk '{print$8}'"
        GET_CPU_FREE = subprocess.getoutput("top -n 1|grep 'id' | head -n 1 |  {0}".format(GET_CPU_CMD))
        print(GET_CPU_FREE)
        NOW_TIME = (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))
        subprocess.getoutput("echo '{0},{1},{2}' >> /data/code/all_ws/ws/{3}-SystemStat.csv".format(NOW_TIME, GET_CPU_FREE, GET_MEM_FREE, HOSTNAME))

def sendReport():
    e = Encryption()
    subject = '系统资源监控'
    smtpserver = 'smtp.qq.com'
    password = e.decrypt(1, "43@36354240443?343@333.44363/383")  #授权码
    test = ("定时检测报告")
    msg = MIMEText(test)
    msg = MIMEMultipart()
    msg['Subject'] = Header(subject, 'utf-8')
    #发送者        # 接受者
    msg['from'] = msg['to'] = account = e.decrypt(1,";0.1>0?0:0<0<09090>061?3?37013=3;3")
    # 附件
    att2 = MIMEText(open('/data/code/all_ws/ws/{}-SystemStat.csv'.format(HOSTNAME), 'rb').read(), 'base64', 'utf-8')
    att2["Content-Type"] = 'application/octet-stream'
    att2["Content-Disposition"] = 'attachment; filename="{}-SystemStat.csv"'.format(HOSTNAME)
    msg.attach(att2)

    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(account, password)
    smtp.sendmail(account, account, msg.as_string())
    smtp.quit()
    return 0

def delete_history_data():
    if subprocess.getoutput("ls /data/code/all_ws/ws/ | grep SystemStat.csv") != "":
        subprocess.getoutput("rm /data/code/all_ws/ws/{}-SystemStat.csv".format(HOSTNAME))

def main():
    ss = SystemStat()
    while True:
        for i in range(0,720):
            ss.timing_record()
            if i == int(719):
                sendReport()
                delete_history_data()
if __name__ == '__main__':
    main()

