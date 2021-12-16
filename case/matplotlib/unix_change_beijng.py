import pandas as pd
import datetime
import time

'''csv = pd.read_csv('task_log_2021-11-30_162731.csv')
time_list = csv['time']
# print(time_list)
for unix in time_list:
    times = datetime.datetime.fromtimestamp(unix)
    print(times)'''

# import time
# a = int(input(time.mktime(time.strptime('%Y-%m-%d %H:%M:%S'))))
# print(a)
import datetime
import time
# while True:
#     time.sleep(2)
    # print(int(time.time(times)))
    # times = datetime.datetime.fromtimestamp(int(time.time()))
    # print(int(time.time()))‘’‘

'''import time

import datetime

dtime = datetime.time

ans_time = int(time.mktime(dtime.timetuple()))
print(ans_time)
'''
import time
def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt
def datetime_timestamp(dt):
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

if __name__ == '__main__':
    a = input(":")
    b = input(':')
    c = datetime_timestamp(a)
    d = datetime_timestamp(b)
    print(c,d)
# s = timestamp_datetime(1332888820)
# print(s)
