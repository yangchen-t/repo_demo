#!/usr/bin/env python3 


# import threading
# import time 


# class TestThreading(threading.Thread):
#     def __init__(self,number2,number3):
#         super().__init__()
#         self.number1 = number2
#         self.number2 = number3

#     def computer(self):
#         # sum = self.number1 + self.number2
#         print("线程",threading.current_thread().getName(),"time",time.strftime('%Y-%m-%d %H:%M:%S'))

#     # def mix(self):
#     #     mix = self.number1 - self.number2
#     #     print(mix)

# if __name__ == "__main__":
#     A = TestThreading( 10, 5)
#     B = TestThreading( 11, 4)
#     C = TestThreading( 12, 3)
#     A.start()
#     A.join()
#     B.start()
#     B.join()
#     C.start()
#     C.join()

#     print("finish!!!!",time.strftime("%Y-%m-%d %H:%M:%S"))
    


#!/usr/bin/env python3 


import time
import threading


class MyThread(threading.Thread):
    def __init__(self,num,number):
        super().__init__()
        self.num = num
        self.number = number
    def run(self):
        print('线程名称：', threading.current_thread().getName(), '参数：', self.num, "参数-2" , self.number , '开始时间：', time.strftime('%Y-%m-%d %H:%M:%S'))
if __name__ == '__main__':
    print('主线程开始时间：',time.strftime('%Y-%m-%d %H:%M:%S'))
    t1 = MyThread(num = 3,number = 1)
    t2 = MyThread(2,2)
    t3 = MyThread(1,3)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    print('主线程结束时间：', time.strftime('%Y-%m-%d %H:%M:%S'))