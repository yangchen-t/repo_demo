from flask import Flask, render_template, request, jsonify
import pandas as pd
from datetime import datetime, time
from queue import Queue
import subprocess
import time
import requests
import os
import urllib.request
import paramiko
import threading

app = Flask(__name__)
progress_queue = Queue()


group_link = "http://devops.qomolo.com/api/devops/ci/integration/group/"
scheme_link = "http://devops.qomolo.com/api/devops/ci/integration/"
repo_link = "https://repo.qomolo.com/repository/"
download_tmp_deb_path = "/tmp/devops/downloads/"
download_deb_path = "/tmp/"

# 读取 CSV 文件
df_system = pd.read_csv('../config/system.csv')
df_project = pd.read_csv('../config/menu.csv')
_ip:str = "192.168.103.172"
_port:int = 10000

class SFTPProgressMonitor:
    def __init__(self, filename, total):
        self.filename = filename
        self.total = total
        self.sofar = 0
        self.lock = threading.Lock()

def upload_progress(callback):
    def decorator(func):
        def wrapper(*args, **kwargs):
            progress_monitor = args[3]  # 这里的索引可能会有所变化，需要根据实际情况调整
            progress_thread = threading.Thread(target=callback, args=(progress_monitor,))
            progress_thread.start()
            return func(*args, **kwargs)
        return wrapper
    return decorator

def start_progress_monitor(progress):
    while True:
        with progress.lock:
            if progress.sofar >= progress.total:
                break
            percentage = min((float(progress.sofar) / progress.total) * 100, 100)
            status = f"Uploading file {progress.filename}: {percentage:.2f}%\r"
            print(status, end="")
        time.sleep(0.1)

    # 当传输完成时，打印最终状态
    status = f"Uploading {progress.filename}: 100.00% \n"
    print(status, end="")

@upload_progress(callback=start_progress_monitor)
def sftp_put_with_progress(sftp, local_path, remote_path, progress_monitor):
    with open(local_path, "rb") as f:
        sftp.putfo(f, remote_path, callback=lambda sent, total: setattr(progress_monitor, 'sofar', sent))

def get_group_id(name, version):
    headers = {
    }
    data = {
        'create_time': [],
        'name': name,
        'version': version,
        'page_num': 1,
        'status': 1,
        'is_delete': 2
    }
    response = requests.post(
        'http://devops.qomolo.com/api/devops/ci/integration/groups', headers=headers, json=data, verify=False)
    data = response.json()
    if data.get('data').get('total') == 0:
        return None
    return data.get('data').get('list')[0].get('id')


def download_deb(pkg, version, repo, arch, save_path):
    chr = pkg[0:1]
    pkg_url = pkg + "_" + version + "_" + arch + ".deb"
    url = os.path.join(repo_link, repo, "pool", chr, pkg, pkg_url)
    save_path = os.path.join(save_path, pkg_url)
    if urllib.request.urlretrieve(url, save_path):
        print("download " + url)


def download_group(group_id):
    response = requests.get(group_link + group_id)
    if response.status_code == 200:
        grp_data = response.json()
        data = grp_data["data"]
        scheme_lst = data["schemes"]
        for scheme in scheme_lst:
            sch_name = scheme["name"]
            sch_version_id = scheme["version_id"]
            sch_version = scheme["version"]
            print("\n\n========Downloading scheme info name:%s version_id:%s version:%s========" % (
                sch_name, sch_version_id, sch_version))
            sch_response = requests.get(scheme_link + str(sch_version_id))
            if sch_response.status_code == 200:
                sch_data = sch_response.json()
                sch_data_dict = sch_data["data"]
                deb_lst = sch_data_dict["module_versions"]
                for deb in deb_lst:
                    pkg_name = deb["pkg_name"]
                    pkg_version = deb["version"]
                    repo_name = deb["repo_name"]
                    arch = "arm64"
                    if deb["arch"] == "all":
                        arch = "all"
                    download_deb(pkg_name, pkg_version,
                                 repo_name, arch, download_tmp_deb_path)
            else:
                exit("failed process scheme " + sch_name)
    else:
        exit("url request failed")

def ensure_two_elements(arr) -> list:
    if len(arr) < 2:
        while len(arr) < 2:
            arr.append("null")
    return arr

def get_non_empty_values_for_datetime(df_system, target_datetime) -> list:
    for index, row in df_system.iterrows():
        if not row.isnull().values.any():  # 检查是否有非空值
            if isinstance(row['Date'], str):
                date_obj = datetime.strptime(row['Date'], '%Y-%m-%d')
            else:
                date_obj = row['Date']
            if date_obj.date() == target_datetime:
                # 仅保留非空值
                infrastructure_person = [cell for cell in row[1:] if pd.notnull(cell)]
                return infrastructure_person
    return ["null"]

def get_duty_personnel() -> list:
    target_date = datetime.now().date()
    print(target_date)
    duty_person = ensure_two_elements(get_non_empty_values_for_datetime(df_system, target_date))
    return duty_person


# 定义路由和视图函数
@app.route('/')
def display_duty_schedule() -> render_template:
    target_date = datetime.now().date()
    duty_person = get_duty_personnel()
    return render_template('duty_schedule.html', in_duty_person=duty_person[0], en_duty_person=duty_person[1])

@app.route('/_information')
def display_csv_data() -> render_template:
    return render_template('display_csv.html', data=df_system.to_html())


@app.route('/_project_information')
def display_project_information() -> render_template:
    return render_template('display_project_information.html', data=df_project.to_html())

@app.route("/get")
def get_input_msg() -> render_template:
    return render_template("input_msg.html")

@app.route('/get_qpilot-group', methods=['POST', 'GET'])
def get_qpilot_group(): # group_name version 
    if request.method == 'POST':
        result = request.form
        group_id = get_group_id(result['group'], result['version'])
        if group_id == None:
            print("group not found")
            exit(1)
        print("group id: " + str(group_id))
        download_group(str(group_id))
        now = time.strftime("%Y%m%d%H%M%S", time.localtime())
        name = result['group'] +"_" + result['version'] + "_" + now + ".zip"
        subprocess.run("zip -jqr "+download_deb_path+name+" "+download_tmp_deb_path, shell=True)
        return render_template("result.html", result=download_deb_path+name)

@app.route('/transmission', methods=['POST', 'GET'])
def transmission_group():
    if request.method == 'POST':
        msg = request.form

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            ssh.connect(msg['ip'], username=msg['host'], password=msg['passwd'])
            sftp = ssh.open_sftp()

            local_file_path = msg['result']
            remote_file_path = "/home/{0}/{1}".format(msg['host'], os.path.basename(local_file_path))

            file_size = os.stat(local_file_path).st_size
            progress = SFTPProgressMonitor(local_file_path, file_size)

            upload_thread = threading.Thread(target=sftp_put_with_progress, args=(sftp, local_file_path, remote_file_path, progress))
            monitor_thread = threading.Thread(target=start_progress_monitor, args=(progress,))
            
            upload_thread.start()
            monitor_thread.start()
            upload_thread.join()
            monitor_thread.join()

        finally:
            if ssh is not None:
                ssh.close()
    return render_template("upload_return.html")

@app.route('/_get_duty_personnel')
def get_updated_duty_personnel() -> str:
    duty_person = get_duty_personnel()
    print(duty_person[0],duty_person[1])
    return duty_person[0]

if __name__ == '__main__':
    app.run(debug=True, host=_ip, port=_port)
