import paramiko,sys

IGV_ID = input(":")
for id in IGV_ID:

    def ssh_params(hostname,port,username,passwd,command):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,passwd)
        stdin, stdout, stderr = ssh.exec_command(command)
        print(stdout.read())
        ssh.close()

    def main():
        # if len(sys.argv) < 2:
        #     print("Please provide csv path.")
        # else:
            ssh_params('10.159.' + id + '.105', 22, 'nvidia',
                       'nvidia','' )

    if __name__ == '__main__':
         main()
