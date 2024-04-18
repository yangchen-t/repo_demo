
import os
import zipfile
import shutil
import time
import datetime
import requests

csv_pdf_files = []
zip_filename =  "dl_{0}.zip".format(
     datetime.datetime.now().strftime("%Y%m%d%H%M%S")
)

# 生成当次实船数据
def make_users(IP):
    data = {
        "truck_id": ["dlqt1","dlqt4","dlqt5"],
        "boat_id": "松云河",
        "start_time": "2024-04-06 14:56:00",
        "end_time": "2024-04-06 17:10:00"
        }
    url = "http://" + IP + "/WellGNS/KPI_PDF"
    response = requests.post(url=url, json=data).text
    print(response)
    print(type(response))

# 移动所有符合list_csv_pdf_files_in_current_directory的文件至destination_path
def move_useless_file(destination_path):
    os.makedirs(destination_path, exist_ok=True)
    for file in csv_pdf_files:
        if os.path.exists(file):
            file_name = os.path.basename(file)
            destination_file_path = os.path.join(destination_path, file_name)
            shutil.move(file, destination_file_path)

# 只当前路径下的所有.csv和.pdf文件
def list_csv_pdf_files_in_current_directory(current_dir):
    for file in os.listdir(current_dir):
        if file.endswith('.csv') or file.endswith('.pdf'):
            file_path = os.path.join(current_dir, file)
            csv_pdf_files.append(file_path)

# 压缩文件
def compressflie(current_dir):
    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in csv_pdf_files:
            print(file)
            if os.path.exists(file):
                file_name = os.path.basename(file)
                os.chdir(current_dir)
                zipf.write(file_name)

def main():
    destination_path = "/tmp/data_bak"
    current_dir = "/home/westwell/workspace/"
    IP = "127.0.0.1:19020"
    make_users(IP)
    time.sleep(10)
    list_csv_pdf_files_in_current_directory(current_dir)
    compressflie(current_dir)
    time.sleep(1)
    move_useless_file(destination_path)

if __name__ == '__main__':
    main()