#!/usr/bin/env python3 

import paramiko 
import subprocess
import os, time, sys
import time as t 
import datetime


ROOT_PATH = "/data/qpilot_log/wellsim"
PASSWD = "qwer"

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
    
    def timer(func):
        def inside(self):
            t1 = time.time()
            func(self)
            t2 = time.time()
            print('task time:{:.2f}s'.format(t2 - t1))
        return inside

    def humanbytes(self,B):
        'Return the given bytes as a human friendly KB, MB, GB, or TB string'
        B = float(B)
        KB = float(1024)
        MB = float(KB ** 2) # 1,048,576
        GB = float(KB ** 3) # 1,073,741,824
        TB = float(KB ** 4) # 1,099,511,627,776
    
        if B < KB:
            return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
        elif KB <= B < MB:
            return '{0:.2f} KB'.format(B/KB)
        elif MB <= B < GB:
            return '{0:.2f} MB'.format(B/MB)
        elif GB <= B < TB:
            return '{0:.2f} GB'.format(B/GB)
        elif TB <= B:
            return '{0:.2f} TB'.format(B/TB)
        
     # TODO: 可视化文件传输 / 未使用
    def progres(self, LOCAL_PATH, sftp, path_ret,FileName, QOMOLO_ROBOT_ID):
        """
        显示上传进度条
        num：已上传大小
        Sum：文件总大小
        #l：定义进度条大小
        """
        print(path_ret,FileName)
        Sum = os.path.getsize(LOCAL_PATH)     # 文件整体大小
        bar_length = 100 # 定义进度条大小
        for i in range(Sum):
            num = self.Realtime_Get_Filesize(sftp, path_ret, FileName, QOMOLO_ROBOT_ID)
            print(num)        # 远端文件大小 
            percent = float(num) / float(Sum)
            hashes = '=' * int(percent * bar_length)  # 定义进度显示的数量长度百分比
            spaces = ' ' * (bar_length - len(hashes))  # 定义空格的数量=总长度-显示长度
            sys.stdout.write(
                "\r传输中: [%s] %d%%  %s/%s " % (hashes + spaces, percent * 100, self.humanbytes(num), self.humanbytes(Sum)))  # 输出显示进度条
            sys.stdout.flush()  # 强制刷新到屏幕
            num = i

    def Realtime_Get_Filesize(self, sftp, path_ret, FileName, QOMOLO_ROBOT_ID):
        for x in sftp.listdir_attr(path_ret + "/" + QOMOLO_ROBOT_ID ):
            print(x)

            if x.filename == FileName + ".tar.gz":
 
                return x.st_size
            else :
                time.sleep(1)
                continue


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
    
    def create_folder(self, QOMOLO_ROBOT_ID, sftp):
        YEAR = str(datetime.datetime.now().year)
        MONTH = str(datetime.datetime.now().month).zfill(2)
        DAY = str(datetime.datetime.now().day).zfill(2)
        YEAR_PATH = ROOT_PATH + "/" + YEAR
        MONTH_PATH = YEAR_PATH + "/" + MONTH
        DAY_PATH = MONTH_PATH + "/" + DAY
        ID_PATH = DAY_PATH + "/" + QOMOLO_ROBOT_ID
        year_existence = True if YEAR in sftp.listdir(ROOT_PATH) else False
        if not year_existence:
            sftp.mkdir(YEAR_PATH)
        month_existence = True if MONTH in sftp.listdir(YEAR_PATH) else False
        if not month_existence:
            sftp.mkdir(MONTH_PATH)
        day_existence = True if DAY in sftp.listdir(MONTH_PATH) else False
        if not day_existence:
            sftp.mkdir(DAY_PATH)
        id_existence = True if QOMOLO_ROBOT_ID in sftp.listdir(DAY_PATH) else False
        if not id_existence:
            sftp.mkdir(ID_PATH)
            print("create "+ ID_PATH)
        return DAY_PATH

    def Data_collect_tar(self, log_path, cmd, FileName):
        if os.path.isdir(log_path):
            os.chdir(log_path)
            subprocess.getoutput(cmd)
        return "/tmp/" + FileName + ".tar.gz"
    
    @timer
    def Upload_nas_file(self):
        print("数据开始打包")
        log_path = "/data/qpilot_sim_lcb_qtruck/qpilot_ws" # 单车数据的绝对路径
        FileName = subprocess.getoutput("hostname") + "-" + datetime.datetime.now().strftime('%Y-%m-%d-%H_%M_%S')
        cmd = "echo qwer | sudo -S tar -zcvf /tmp/{}.tar.gz *.log*" .format(FileName)  # 对应的指令
        LOCAL_PATH = self.Data_collect_tar(log_path, cmd, FileName)
        QOMOLO_ROBOT_ID = "wellsim"
        print("本地压缩包路径： ",LOCAL_PATH)
        sftp = self.Sftp_create()
        path_ret = self.create_folder(QOMOLO_ROBOT_ID,sftp)
        REMOTE_PATH = os.path.join(path_ret + "/" + QOMOLO_ROBOT_ID, FileName + ".tar.gz")
        sftp.put(LOCAL_PATH, REMOTE_PATH) # callback=self.progres(LOCAL_PATH, sftp, path_ret, FileName, QOMOLO_ROBOT_ID)
        print("\033[0;31;40mUpload finish, Nas PATH: {0}\033[0m".format(REMOTE_PATH))


def main():
    encryption = Encryption()
    HOST = encryption.decrypt(66, "/474?3;3/40464;3/4.4@3;31414")
    USERNAME = encryption.decrypt(44, "62:1/271@172/271@10.1291>171")
    PASSWORD = encryption.decrypt(33, "/3/3;2=1@1=112;1>../@.=.=.")
    PORT = 22
    FAD = FileAutoDownload(HOST, PORT, USERNAME, PASSWORD)
    FAD.Upload_nas_file()



if __name__ == '__main__':
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd == "-r":
                subprocess.getoutput("echo {0} | sudo -S rm /tmp/*.tar.gz".format(PASSWD))
            else:
                print(" -r     = delete log history")
        else:
            main()
