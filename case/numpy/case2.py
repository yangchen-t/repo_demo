import numpy as np
import pandas as pd
# import os

# a = np.arange(8)
# print('原始数组：')
# # print(a)
# print('\n')
# b = a.reshape(2, 4)
# print('修改后的数组：')
# print(b)

# a = np.arange(9).reshape(3,3)
# print(a)
# print ('原始数组：')
# for row in a:
#     print (row)
# 对数组中每个元素都进行处理，可以使用flat属性，该属性是一个数组元素迭代器：
# print ('迭代后的数组：')
# for element in a.flat:
#     print (element)

# a = np.arange(8).reshape(2, 4)
# print('原数组：')
# print(a)
# print('\n')
# 默认按行
# print('展开的数组：')
# print(a.flatten())
# print('\n')
# print('以 F 风格顺序展开的数组：')
# print(a.flatten(order='F'))

a = np.arange(8).reshape(2, 4)
print('原数组：')
print(a)
print('\n')
print('调用 ravel 函数之后：')
print(a.ravel())
print('\n')
print('以 F 风格顺序调用 ravel 函数之后：')
print(a.ravel(order='F'))

