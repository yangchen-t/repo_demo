import subprocess 
from datetime import datetime, timedelta
# moduleList = []

# def select(file):
#     module = subprocess.getoutput("cat {0} | awk -F ',' '{1}'".format(file, '{print$7}'))
#     print(module)
#     moduleList = module.split()
#     return moduleList

# newlist = (set(select("test.log")))

# for i in newlist:
#     print("#"*10, i , "#"*10)
#     print(subprocess.getoutput("cat {0} | grep {1}".format("./test.log", i)))

# moduleList.clear()

time_str = '04:14:00'
start_time = datetime.strptime(time_str, '%H:%M:%S')

increment = timedelta(seconds=1)
current_time = start_time

moduleList = []

for _ in range(600):  # 逐秒增加 10 次
    current_time += increment
    new_time_str = current_time.strftime('%H:%M:%S')
    # print(new_time_str)
    print(subprocess.getoutput("cat {0} | grep {1} | grep %memused -A 1 | tail -n 1 | awk '{2}' >> Usedmem.csv".\
                               format("../sar.log",new_time_str, """{print$1$2" "$3","$7","$8","$9","$10","$11","$12}""" )))