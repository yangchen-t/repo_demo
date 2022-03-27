#!/bin/python3

import pandas as pd
import numpy as np
import datetime,logging

csv_file = pd.read_csv('task_log_2021-11-22_141220.csv')    ##
v_1 = 0.000
t_1 = (1637590347)      ##
t_2 = (1637605857)      ##
res = csv_file[(csv_file["time"] > float(t_1)) & (csv_file["time"] < float(t_2))]
time_less = res[(res["speed(mps)"] < float(v_1))]
times = time_less['time']
speed = time_less['speed(mps)']

for time,current_v in zip(times,speed):
        beijing_times = datetime.datetime.fromtimestamp(time)
        # print('{0}, {1}, {2}'.format(current_v,time,beijing_times))
        # logger =  (speed<0)
        logging.basicConfig(level=logging.DEBUG,#控制台打印的日志级别
                    filename='upload.log',
                    filemode='w',##有w和a，w就是写模式，每次都会重新写日志 #a是追加模式，默认如果不写的话，就是追加模式
                    format=
                    '{ %(created)f- %(funcName)s -  [%(levelname)s] }:= %(message)s'
                    #日志格式
                    )
        logging.debug('{0}, {1}, {2}'.format(current_v,time,beijing_times))
#logging.debug('最大的负速度为:'+str(min(speed)))
