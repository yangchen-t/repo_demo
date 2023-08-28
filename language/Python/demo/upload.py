#/usr/bin/env python3 

import argparse
import paramiko
import time as t 
import os 
import sys


Ignore = "rosbag"

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


class FileUpload(object): 
     
    def __init__(
        self, ip , port, username, passwd
        ) -> None:  

        self.passwd = passwd
        self.username = username
        self.port = port
        self.ip = ip 

        self.LocalDirList = []
        self.LocalFileList = []
        self.RemoteDirList = []
        self.RemoteFileList = []
        self.AllFile = []

   # create sftp connect
    def Sftp_create(self):
        for i in range(10):
            try:
                transport = paramiko.Transport(self.ip, self.port)
                transport.connect(username=self.username, password=self.passwd)
                sftp = paramiko.SFTPClient.from_transport(transport)
                print("sftp -> create")
                return sftp
            except Exception as e:
                print("sftp -> error:{}".format(e))
                print("retry connect.....")
                t.sleep(2)
        return None


    def LocalFileMatch(self, LocalPath,RemotePath):
        if os.path.isdir(LocalPath):
            for root, dirs, files in os.walk(LocalPath): 
                for d in dirs:
                    if d == Ignore:
                        continue 
                    basePath = root[len(LocalPath):len(root)]
                    self.LocalDirList.append(os.path.join(basePath,d))
                for f in files:
                    if Ignore in str(root):
                        continue
                    basePath = root[len(LocalPath):len(root)]
                    self.LocalFileList.append(os.path.join(basePath,f)) # 相对路径
                    self.AllFile.append(os.path.join(root,f))           # 绝对路径
            for d in self.LocalDirList:
                if d[0] == "/":
                    d = d[1:]
                self.RemoteDirList.append(os.path.join(RemotePath, d))
            for f in self.LocalFileList:
                if f[0] == "/":
                    f = f[1:]
                self.RemoteFileList.append(os.path.join(RemotePath,f))
        else:
            print("{0} is error".format(LocalPath))
            exit(-1)

    def RemotePathCreate(self,RemotePath): 
        sftp = self.Sftp_create()
        try:
            sftp.mkdir(RemotePath)
        except OSError: pass

        for Rdir in self.RemoteDirList:
            try:
                sftp.stat(Rdir)
                print(Rdir, " --> exist")
            except FileNotFoundError:
                print("mkdir --> ", Rdir)
                sftp.mkdir(Rdir)

    def UploadNas(self):
        sftp = self.Sftp_create()
        for l,r in zip(self.AllFile, self.RemoteFileList):
            try:  
                if sftp.stat(r).st_size == os.stat(l).st_size: pass
            except FileNotFoundError:
                print("upload: ",r)
                sftp.put(l,r)


def funcArgparse():
    my_arg = argparse.ArgumentParser('My argument parser')
    my_arg.add_argument('--module','-m', type=str, help='input module name')
    my_arg.add_argument('--filepath','-f', type=str, help='input file path')
    my_arg.add_argument('--template', '-t', type=str, help='python3 {0} -f "/home/westwell/Desktop" -m planning'.format(sys.argv[0]) )
    args = my_arg.parse_args()
    return args

def checkArgs():
    if funcArgparse().filepath is None:
        print("<< You need to specify a local path, you can try --filepath xxx or -F xxx >>")
        exit(-1)
    if funcArgparse().module is None:
        print("<< operation error, lack module args, you can try --module xx or -M xx >>")
        exit(-1)

def main():
    checkArgs()
    RemotePath = "/data/qtest/regression/" + funcArgparse().module + "/QA_candidate_testcases"
    encryption = Encryption()
    HOST = encryption.decrypt(66, "/474?3;3/40464;3/4.4@3;31414")
    PORT = 22
    USERNAME = encryption.decrypt(44, "62:1/271@172/271@10.1291>171")
    PASSWORD = encryption.decrypt(33, "/3/3;2=1@1=112;1>../@.=.=.")
    fu = FileUpload(HOST, PORT, USERNAME, PASSWORD)
    fu.LocalFileMatch(funcArgparse().filepath, RemotePath)
    fu.RemotePathCreate(RemotePath) 
    fu.UploadNas()

if __name__ == '__main__':
    main()