#!/usr/bin/env python3 

import paramiko
import time

class GatewayRestartTun0(object):
    def __init__(self) -> None:
        self.hostname="10.159.8.1"
        self.port = 22
        self.username = "qomolo"
        self.passwd = self.decrypt(66, '@/>/>0/00.=0/090>003')  

    def decrypt(self,ksa, s):
        if len(bytearray(str(s).encode("utf-8"))) % 2 != 0:
            return ""
        b = bytearray(len(bytearray(str(s).encode("utf-8"))) // 2)
        j = 0
        for i in range(0, len(bytearray(str(s).encode("utf-8"))) // 2):
            c1 = (bytearray(str(s).encode("utf-8"))[j]) - 46 
            c2 = (bytearray(str(s).encode("utf-8"))[j + 1]) -46 
            j += 2
            b[i] = (c2 * 19 + c1) ^ ksa
        return b.decode("utf-8")


    def restart_gateway_tun0_func(self, type_operation="restart"):
            cmd = "echo  {0} | sudo -S systemctl {1} openvpn-client@CTN_WS_8.service".format(
                    self.passwd, type_operation)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(self.hostname, self.port, self.username, self.passwd)
            stdin,stdout,stderr = ssh.exec_command(cmd)
            stdin.write("Y")  
            print(stdout.read().decode())
            ssh.close()


if __name__ == "__main__":
    grt0 = GatewayRestartTun0()
    grt0.restart_gateway_tun0_func()
    time.sleep(1)
    print("restart finish")
