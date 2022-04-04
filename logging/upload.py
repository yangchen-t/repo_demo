#!/bin/python3
import logging

while True:
    data = input('please:')
    print(data)
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        filename='case.txt',
                        filemode='w',  ##有w和a，w就是写模式，每次都会重新写日志 #a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '{ %(created)f- %(funcName)s - %(name)s - [%(levelname)s] }:= %(message)s'
                        # 日志格式
                        )
    logging.debug('{0}'.format(data))





