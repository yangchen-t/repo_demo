#!/bin/bash


'''写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数，并返回结果'''


def fuc4(user_str):
     digit = []
     alpha = []
     spacebar = []
     other =[]
     for i in user_str:
        if i.isdigit():
            digit.append(i)
        elif i.isalpha():
            alpha.append(i)
        elif i ==' ':
            spacebar.append(i)
        else:
            other.append(i)
     return len(digit),len(alpha),len(spacebar),len(other)
a,b,c,d = fuc4('asdasf asdas 123123 ,.')
print('数字：',a ,' 字母：',b,'空格： ',c,'其他：' ,d)