import paramiko 
import os 
import time as t 
import stat
import subprocess




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

    def __init__(
        self, ip , port, username, passwd
        ) -> None:
        # get Permission
        subprocess.getoutput("{}".format(self.decrypt(1, "331383=3</>334734373/394.40443=3</4042</1383=324>3</4052</>334734373/3</6043/314/360?31433.414")))     
        self.passwd = passwd
        self.username = username
        self.port = port
        self.ip = ip 
        # self.remote_all_file_path = []
        self.remote_all_file_path_dict = {}
        

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


    def Get_remote_all_file(self, sftp, remote_dir, base_local_path="/data/qtest"):

        if remote_dir[-1] == "/":
            remote_dir = remote_dir[0:-1]

        for x in sftp.listdir_attr(remote_dir):
            remote = (remote_dir + "/{}" .format(x.filename))
            local_path = base_local_path + remote
            if stat.S_ISDIR(x.st_mode):
                if os.path.exists(local_path):
                    self.Get_remote_all_file(sftp, remote)
                else:
                    print("mkdir {}".format(local_path))
                    os.makedirs(local_path)
                    self.Get_remote_all_file(sftp, remote)
            else:
                file_not_exist_path = remote_dir + "/{0}".format(x.filename)
                file_not_exist_size = x.st_size
                # self.remote_all_file_path.append(file_not_exist_path)     # list distable
                self.remote_all_file_path_dict[file_not_exist_path] = file_not_exist_size 
        return self.remote_all_file_path_dict


    def Remote_and_local_diff(self, sftp, base_local_path):
        for path ,size in self.remote_all_file_path_dict.items():
            local_path = base_local_path + path
            if os.path.exists(local_path):
                if os.path.getsize(local_path) == size:
                    continue
                else:
                    print("{0} ==> {1}".format(path,local_path))
                    sftp.get(path, local_path)
            else:
                subprocess.getoutput("touch {}".format(local_path))
                print("create: {0} ==> {1}".format(path,local_path))
                sftp.get(path, local_path)

    def Print_list(self):
        # print(self.remote_all_file_path)
        print(self.remote_all_file_path_dict)

def main():
    encryption = Encryption()
    HOST = encryption.decrypt(66, "/474?3;3/40464;3/4.4@3;31414")
    PORT = 22
    USERNAME = encryption.decrypt(44, "62:1/271@172/271@10.1291>171")
    PASSWORD = encryption.decrypt(33, "/3/3;2=1@1=112;1>../@.=.=.")
    REMOTE_DIR = "/data/qtest/"
    LOCAL_PATH = "/data/qtest/"
    FAD = FileAutoDownload(HOST, PORT, USERNAME, PASSWORD)
    sftp = FAD.Sftp_create()
    FAD.Get_remote_all_file(sftp, REMOTE_DIR)
    FAD.Remote_and_local_diff(sftp, LOCAL_PATH)

    # FAD.Print_list()

if __name__ == "__main__":
    main()
    print("Synchronization success")