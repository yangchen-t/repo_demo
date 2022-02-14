import paramiko,sys


def ssh_params(hostname,port,username,passwd,command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname,port,username,passwd)
    stdin,stdout,stderr = ssh.exec_command(command)
    print(stdout.read())
    ssh.close()

def main():
    if len(sys.argv) < 2:
        print("Please provide csv path.")
    else:
        ssh_params('10.159.' + sys.argv[1] + '.105', 22, 'nvidia', 'nvidia', 'dpkg -l | grep qpilot')

if __name__ == '__main__':
     main()
