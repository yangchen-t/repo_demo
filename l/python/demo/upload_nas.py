#!/usr/bin/env python3 


import paramiko 
import subprocess
import sys, os 
import time as t 


class Encryption():

    def __init__(self) -> None:
        pass    
        
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


class FileAutoDownload(Encryption):

    index = 0 
    def __init__( self, ip , port, username, passwd) -> None:
        self.passwd = passwd
        self.username = username
        self.port = port
        self.ip = ip 
        
    # create connect
    def Sftp_create(self):
        for i in range(10):
            try:
                transport = paramiko.Transport(self.ip, self.port)
                transport.connect(username=self.username, password=self.passwd)
                sftp = paramiko.SFTPClient.from_transport(transport)
                print("create sftp connect success")
                return sftp
            except Exception as e:
                print("sftp connect error:{}".format(e))
                print("retry connect.....")
                t.sleep(2)
        return None
    def Remote_path_exist(REMOTE):
        pass

    def Data_collect_tar(log_path):
        os.path.isdir(log_path)



    def Upload_nas_file(self, sftp, LOCAL_PATH, REMOTE_PATH):
        sftp.put(LOCAL_PATH, REMOTE_PATH)



def main():
    encryption = Encryption()
    HOST = encryption.decrypt(66, "/474?3;3/40464;3/4.4@3;31414")
    USERNAME = encryption.decrypt(44, "62:1/271@172/271@10.1291>171")
    PASSWORD = encryption.decrypt(33, "/3/3;2=1@1=112;1>../@.=.=.")
    PORT = 22
    FAD = FileAutoDownload(HOST, PORT, USERNAME, PASSWORD)
    sftp = FAD.Sftp_create()
    log_path = "" # 单车数据的log
    REMOTE_DIR = "/data/report"
    FAD.Upload_nas_file(sftp,log_path,REMOTE_DIR)


if __name__ == '__main__':
        main()
