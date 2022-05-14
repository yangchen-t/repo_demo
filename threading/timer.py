#!/usr/bin/env python3 


# 单次执行
from threading import Timer
import time

def computer():
    for i in range(10):
        print(i)
        if i > 5:
            print("change-speed")
            time.sleep(2)
def work():
    print("Hello Python")
# 5 秒后执行 work 方法
t1 = Timer(1, computer)
t1.start()
t = Timer(5, work)
t.start()
t.join()