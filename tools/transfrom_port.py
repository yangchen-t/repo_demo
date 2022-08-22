import paramiko
import base64
import sys


key = b'Z2F0ZUB3ZXN0Iw=='
port = 22
username = "qomolo"
passwd = base64.b64decode(key).decode()

def transfrom_func():
    try:
        vehicle_ip,ip = sys.argv[2],sys.argv[1]
        cmd = "echo  {0} | sudo -S iptables -t nat -A PREROUTING -p tcp --dport 4000 -j DNAT --to-destination {1}:4000".format(passwd,vehicle_ip)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,port,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(cmd)
        print(stdout.read().decode())
        ssh.close()
    except:
        print('ERROR',ip)

def Doc_func():
        print('''
        需要添加参数：
        python3 transfrom_port.py  4Gip 车辆ip
        ''')

def main():
    if len(sys.argv) < 2:
        print("command not unknow.")
        Doc_func()
    else:
        transfrom_func()
        print("finish")
        

if __name__ == "__main__":
    main()
    


