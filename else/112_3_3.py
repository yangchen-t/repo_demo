#/usr/bin/env python3

'''
Remove specified number
'''


num = int(input('please enter 0~9 numbers :'))

for num_1 in range(1,101):
    if str(num) in str(num_1):
        continue
    print(num_1)

    