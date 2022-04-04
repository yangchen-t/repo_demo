# -*- coding: utf-8 -*-
#!/usr/bin/env python3 

import paramiko,threading
import sys


def ssh2(ip, username, passwd, cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=5)
        ssh.exec_command(cmd)
        stdin.write("Y")   #简单交互，输入"y"
        ssh.close()
    except:
        print('%s\tError\n' % (ip))


if __name__ == '__main__':
    cmd = ['docker exec -it ppc_igv bash "supeervisord stop mqtt_agent"']
    username = "nvidia"  # 用户名
    passwd = "nvidia"  # 密码
    threads = []  
    print("Begin......")
    ip = '10.159.' +sys.argv[1] + '.105'
    a = threading.Thread(target=ssh2, args=(ip, username, passwd, cmd))
    a.start()


