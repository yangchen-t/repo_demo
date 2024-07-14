#!/usr/bin/env python3 

import time
import threading
def work(num):
    print('线程名称：',threading.current_thread().getName(),'参数：',num,'开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == '__main__':
    print('主线程开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
    t1 = threading.Thread(target=work,args=(3,))
    t2 = threading.Thread(target=work,args=(2,))
    t3 = threading.Thread(target=work,args=(1,))
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join() 
    t3.join()       # join 方法阻塞主线程，等待当前线程运行结束
    print('主线程结束时间：', time.strftime('%Y-%m-%d %H:%M:%S'))