#!/usr/bin/env python3 


import threading
import time
import os
def fun1(number):
    for i in range(number):
        print("1",i)
        # time.sleep(1)

def fun2(number):
    for i in range(number):
        print('2',i)
        # time.sleep(3)


if __name__ == '__main__':
    for i in range(10):
        sing_thread = threading.Thread(target=fun1,args=(i,))
        song_thread = threading.Thread(target=fun2,args=(10,))

        sing_thread.start()
        song_thread.start()
