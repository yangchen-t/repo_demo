#!/bin/python3

import logging
while True:
    money = input('输入每月工资：')
    def sum(house, kaizhi, fangzhu):
        if int(money) <= int(0) :
                print('请输入正确的数量')
                # exit(404)
        money_sum = int(money) - int(house) - int(kaizhi) - int(fangzhu)
        money_sum_all = money_sum*12
        print(money_sum_all)
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                    filename='demo_sum.log',
                    filemode='w',  ##有w和a，w就是写模式，每次都会重新写日志 #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '{ %(created)f- %(funcName)s -  [%(levelname)s] }:= %(message)s'
                    # 日志格式
                    )
    sum(house= 2700,kaizhi= 1000,fangzhu= 500)