# import pandas as pd
# import datetime
# import time

'''csv = pd.read_csv('task_log_2021-11-30_162731.csv')
time_list = csv['time']
# print(time_list)
for unix in time_list:
    times = datetime.datetime.fromtimestamp(unix)
    print(times)'''

# import time
# a = int(input(time.mktime(time.strptime('%Y-%m-%d %H:%M:%S'))))
# print(a)
# import datetime
# import time
# while True:
#     time.sleep(2)
    # print(int(time.time(times)))
    # times = datetime.datetime.fromtimestamp(int(time.time()))
    # print(int(time.time()))‘’‘
import sys

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
    s = time.mktime(time.strptime(dt,'%Y-%m-%d %H:%M:%S'))
    return int(s)

if __name__ == '__main__':
    # for a in ['2021-10-10 20:10:20','2021-12-02 10:20:10']:
        # c = str(datetime_timestamp(sys.argv[1]))
        # a = sys.argv[1]
        a = input(':')
        b = input(':')
        d = datetime_timestamp(a)
        c = datetime_timestamp(b)
        print(a,b,
              c,d)

