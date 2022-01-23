#!/bin//python3


'''写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。'''

def length(number):
    if len(number) > 2 :
        print(number[:2])
    return len(number)
a = length([1,22,3,4,1,3])
print('sum',a)