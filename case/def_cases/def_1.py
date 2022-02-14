#!/bin/bash
'''编写一个名为collatz()的函数,它有一个名为number的参数
   如果参数是偶数,那么collatz()就打印出number//2
   如果number是奇数,collatz()就打印3*number+1'''

def collatz(number):
    if number % 2 != 0 :
        b = 3 * number + 1
        print(b)
    else :
        a = number // 2
        print(a)
collatz(number=12)

