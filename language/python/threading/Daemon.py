#!/usr/bin/env python3 

# 不设置守护线程
import threading


def work(num):
    for i in range(num):
        print(threading.current_thread().name + "  " + str(i))
t = threading.Thread(target=work, args=(10,), name='守护线程')
t.start()
for i in range(6):
    pass
    # print(i)
    
# 输出结果：
'''
守护线程  0
守护线程  1
守护线程  2
守护线程  3
守护线程  4
守护线程  5
守护线程  6
守护线程  7
守护线程  8
守护线程  9
'''





