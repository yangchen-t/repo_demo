import subprocess 
from datetime import datetime, timedelta

time_str = '04:14:00'
start_time = datetime.strptime(time_str, '%H:%M:%S')

increment = timedelta(seconds=1)
current_time = start_time

moduleList = []

file = "../newmem.log"
output = "test.log"

def select(file,ts):
    module = subprocess.getoutput("cat {0} | grep {1} | {2}".format(file, ts, "awk '{print$12}'"))
    moduleList = module.split()
    return moduleList

for _ in range(600):  # 逐秒增加 10 次
    current_time += increment
    new_time_str = current_time.strftime('%H:%M:%S')
    print(new_time_str)
    # time.sleep(1)
    newList = set(select(file=file ,ts=new_time_str))
    for i in newList:
        subprocess.getoutput("/usr/bin/cat {0} | grep {1} | grep {2} | head -n 1 | {3} >> mem.csv".\
                                format(file, new_time_str, i,"""awk '{print$1$2" "$3","$6","$7","$8","$9","$10","$11","$12}'"""))
 
    moduleList.clear()
    newList.clear()  