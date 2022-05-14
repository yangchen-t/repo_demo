import paramiko


igv_id = [21,22,23,24,25,26,27,28,29,30,31,32,33,73,76]
port = 22
username = "nvidia"
passwd = "nvidia"
command = "cat /opt/qomolo/qpilot/share/qpilot_parameters/agent/agent.yaml | grep line_speed -A2 "

for ID in igv_id:
    try:
        hostname=str('10.159.'+ str(ID) +'.105')
        print(hostname,"---> ---> ---> ---> ")
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname,port,username,passwd)
        stdin,stdout,stderr = ssh.exec_command(command)
        print(stdout.read().decode())
        ssh.close()
    except:
        print('ERROR',hostname)

