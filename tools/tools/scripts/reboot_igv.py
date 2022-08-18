import paramiko


igv_id = [1,2,21,22,23,24,25,26,27,28,29,30,31,32,33,72,73,76]
port = 22 
username = "nvidia"
passwd = "nvidia"
command = "/opt/qomolo/utils/qpilot_setup/all_supervisord/start_container.sh"



def reboot_igv(hostname,port,username,passwd,command):
    try:
        print(hostname,"---> ---> ---> ---> ")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.close()
    except:
        print('ERROR',hostname)


if __name__ == "__main__":
    print("重启单个还是全部(0/1)")
    number = input(":")
    if number == str(1):
        for i in igv_id:
            ip = "10.159."+str(i)+".105"
            reboot_igv(ip,port,username,passwd,command)
    elif number == str(0):
        igv_list = str(input("请输入单车序号:")).split()
        for i in igv_list:
            ip = str("10.159."+str(i)+".105")
            print(ip)
            reboot_igv(ip,port,username,passwd,command)
    else:
        print("please input 0 or 1")
