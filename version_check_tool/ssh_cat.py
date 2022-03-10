import paramiko




def sshclient_execmd(hostname, port, username, password, execmd):
        s = paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname=hostname, port=port, username=username, password=password)
        stdin, stdout, stderr = s.exec_command(execmd)
        stdin.write("Y")            # Generally speaking, the first connection, need a simple interaction.
        print(stdout.read().decode())
        s.close()

def main():
        IGV_ID = [21, 22]
        for ID in IGV_ID:
                hostname = str('10.159.' + str(ID) + '.105')
                print(hostname)
                port = 22
                username = 'nvidia'
                password = 'nvidia'
                execmd = [str('cat /opt/qomolo/utils/qpilot_setup/all_supervisord/.env | grep MQTTNAMESPACE -A2'),
                          str('cat /opt/qomolo/qpilot/qpilot/share/qpilot_parameters/agent/agent.yaml | grep line_speed -A3')]
                for cmd in execmd:
                        sshclient_execmd(hostname, port, username, password, cmd)
if __name__ == "__main__":
        main()