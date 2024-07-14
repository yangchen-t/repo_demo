import requests
import json, yaml, sys

last_mode=0
strongest_mode=1
dual_mode=2
first_mode=3

veh_profile="/etc/qomolo/profile/vehicle_type/profile.yaml"

mode_list = {
    last_mode:      "last return",
    strongest_mode: "strongest return" ,
    dual_mode:      "dual return",
    first_mode:     "first return"
}

def lidar_number_list():
    try:
        with open(veh_profile, 'r') as file:
            config = yaml.safe_load(file)
    except FileNotFoundError:
        print("{0} file is exist".format(veh_profile))
        sys.exit(-1)
    if isinstance(config, dict):
        lidar_ips = [item['ip'] for item in config.get('hardware', {}).get('lidar', [])]
        ip_list_no_cidr = [ip.split("/")[0] for ip in lidar_ips]
        return ip_list_no_cidr
    else:
        print("YAML configuration could not be loaded properly.")
        sys.exit(-1)

def get_current_mode(hesai_ip):
    url = 'http://{ip}/pandar.cgi?action=get&object=lidar_data&key=lidar_mode'.format(ip=hesai_ip)

    response = requests.get(url)
    print(hesai_ip, ":" ,mode_list[int(json.loads(response.text)["Body"]["lidar_mode"])])
    if (int(json.loads(response.text)["Body"]["lidar_mode"]) == first_mode):
        return True
    else:
        return False

def set_mode(hesai_ip, set_m):
    url = 'http://{ip}/pandar.cgi?action=set&object=lidar_data&key=lidar_mode&value={mode}' .format(ip=hesai_ip, mode=set_m)

    response = requests.get(url)
    print(response.text)  

def set_reboot(hesai_ip):
    url = 'http://{ip}/pandar.cgi?action=set&object=reboot'.format(ip=hesai_ip)
    response = requests.get(url)
    print(response.text)  

def usages():
    print("""Usage:ython3 {} [option]
Options:
    adjust: adjust lidar mode
    reset : force reset first return mode
    reboot: reboot lidar""".format(sys.argv[0]))

def main():
    _lidarlist = lidar_number_list()
    try:
        args1 = sys.argv[1]
    except IndexError:
        for i in _lidarlist:
            get_current_mode(i)   
        sys.exit(0)

    if args1 == "adjust":
        while True:
            print(mode_list);r = int(input(":"))
            if r in mode_list:
                for i in _lidarlist:
                    set_mode(i, r)
                break
            else:
                print("输入错误 [0~3]")
    elif args1 == "reset":
        for i in _lidarlist:
            set_mode(i, first_mode)
    elif args1 == "reboot":
        ip = input("输入激光ip: ")
        set_reboot(ip)
    else:
        usages()

if __name__ == '__main__':
    main()