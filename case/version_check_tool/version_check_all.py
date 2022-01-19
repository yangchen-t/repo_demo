import paramiko

IGV_ID = [1,2,3,4,5,6]
for ID in IGV_ID:
        try:
                IP=str('10.159.'+ str(ID) +'.105')
                print(IP)
                def ssh_params(hostname,port,username,passwd,command):
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        ssh.connect(hostname,port,username,passwd)
                        stdin,stdout,stderr = ssh.exec_command(command)
                        print(stdout.read())
                        print(stderr.read())
                        ssh.close()
                ssh_params(IP, 22, 'nvidia', 'nvidia', 'cat /data/code/all_ws/ws/install/fpal_uniformar/share/fpal_uniformar/config/igv_control.yaml')
        except:
                print('ERROR')