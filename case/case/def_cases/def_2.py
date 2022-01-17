#!/bin/python3
'''编写一个函数cacluate, 可以接收任意多个数,返回的是一个元组.
     元组的第一个值为所有参数的平均值, 第二个值是大于平均值的所有数'''


def cacluate(*number):
    list = []
    count_number_1 = sum(*number) // len(*number)

    if  big_data > count_number_1 :
        list[1] = big_data
        list[0] = count_number_1

