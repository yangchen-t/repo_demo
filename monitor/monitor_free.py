#!/usr/bin/env python3

import subprocess
import smtplib
from email.mime.text import MIMEText
from email.header import Header



get_free = "awk '{print $4}'  | cut -f 1 -d 'G'"
real_free = subprocess.getoutput("echo nvidia | sudo -S df -h | grep /data| grep -v docker | {0}" .format(get_free))

def sendReport():
    subject = '回归环境系统资源监控'
    smtpserver = 'smtp.qq.com'
    password = 'dpfxwudqdpesdfah'  #授权码
    test = ("剩余资源: {0}".format(real_free))
    msg = MIMEText(test)
    msg['Subject'] = Header(subject, 'utf-8')
    #发送者        # 接受者
    msg['from'] = msg['to'] = account = decrypt(11,".1;01121@03131010111@16464@/733353")
   
    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(account, password)
    smtp.sendmail(account, account, msg.as_string())
    smtp.quit()
    return 0

def decrypt(ksa, s):
    c = bytearray(str(s).encode("utf-8"))
    n = len(c)
    if n % 2 != 0:
        return ""
    n = n // 2
    b = bytearray(n)
    j = 0
    for i in range(0, n):
        c1 = c[j]
        c2 = c[j + 1]
        j = j + 2
        c1 = c1 - 46
        c2 = c2 - 46
        b2 = c2 * 19 + c1
        b1 = b2 ^ ksa
        b[i] = b1
    return b.decode("utf-8")

def main():
    if (real_free < int(20)):
        sendReport()

if __name__ == "__main__":
    main()




