#################
#多人发送文本文件
#################
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import subprocess

def sendReport():
    #发送邮箱
    sender = '2876355007@qq.com'
    #接收邮箱
    # receivers = ['1910518222@qq.com','2339891600@qq.com']   #多人发送
    receiver = '2876355007@qq.com'  #单人发送
    #发送邮件主题
    subject = '定时检测系统资源报告'
    #发送邮箱服务器
    smtpserver = 'smtp.qq.com'
    #发送邮箱用户/密码
    username = '2876355007@qq.com'
    password = 'dpfxwudqdpesdfah'#授权码
    #中文需参数‘utf-8’，单字节字符不需要
    #编写HTML类型的邮件正文
    test = subprocess.getoutput("cat new_upload.sh")
    msg = MIMEText(test)
    #主题固定属性
    msg['Subject'] = Header(subject, 'utf-8')
    #发送者
    msg['from'] = sender
    # 接受者
    msg['to'] = receiver
    #连接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(username, password)
    # smtp.sendmail(sender, receivers, msg.as_string())
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

sendReport()
