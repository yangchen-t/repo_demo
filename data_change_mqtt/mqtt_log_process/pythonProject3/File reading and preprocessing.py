import time
import datetime

timestamp = '20210822T084037Z'

def timestamp_to_time(timestamp):
    # timearray = time.strptime(timestamp, "%Y%m%dT%H%M%SZ")
    stamp = time.mktime(time.strptime(timestamp,'%Y%m%dT%H%M%SZ'))
    # print(stamp)
    delta = 8 * 3600.0
    new_stamp = stamp + delta
    local_time = time.localtime(new_stamp)

    otherstyletime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    return otherstyletime

print(timestamp_to_time(timestamp))