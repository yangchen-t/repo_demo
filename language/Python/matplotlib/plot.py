#!/usr/bin/env python3

from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
import pandas as pd
import time
import params



def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def datetime_timestamp(dt):
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)


class CsvReadPlot():
    def __init__(self,csv_1,csv_2,time_start,time_stop):
        self.csv_1 = csv_1
        self.csv_2 = csv_2
        self.time_start = time_start
        self.time_stop = time_stop
        self.time = time

    def csv_change(self):
        csv1_file = pd.read_csv(self.csv_1)
        csv2_file = pd.read_csv(self.csv_2)

        csv_1_res = csv1_file[(csv1_file['time'] > float(self.time_start)) &
                              (csv1_file['time'] < float(self.time_stop))]
        csv_2_res = csv2_file[(csv2_file['time'] > float(self.time_start)) &
                              (csv2_file['time'] < float(self.time_stop))]

        x,y,v,t_new = csv_1_res['x'],csv_1_res['y'],csv_1_res['speed(mps)'],csv_1_res['time']
        current_v,output_v,speed_time = csv_2_res['current_speed'],csv_2_res['output_speed'],csv_2_res['time']

        plt.figure('This is the first table')
        ax = plt.gca()        # get current axes
        # ax.spines['right'].set_color('none')
        # ax.spines['top'].set_color('none')
        plt.title('X,Y-diagram ')
        plt.xlabel(' X '), plt.ylabel('Y')
        x_1_major_locator, y_1_major_locator = MultipleLocator(5), MultipleLocator(10)
        ax.yaxis.set_major_locator(x_1_major_locator), ax.yaxis.set_major_locator(y_1_major_locator)
        plt.plot(x, y, ls="-", color='blue', marker='',label = '')
        # plt.legend()
        plt.grid()

        plt.figure('This is the second table')
        ax = plt.gca()
        ax.spines['right'].set_color('none'), ax.spines['top'].set_color('none')
        plt.title('speed diagram')
        plt.xlabel(' time '), plt.ylabel('V')
        # fig = plt.figure(1, facecolor='white')
        # fig.clf()
        # plt.annotate('stopcommand',(0.38, 0.04), (0.6, 0.5), va="center",  ha="center",       #tab
        #             xycoords="axes fraction", textcoords="axes fraction",
        #             bbox=dict(boxstyle="sawtooth", fc="0.8"), arrowprops=dict(arrowstyle="<-"))
        # plt.annotate(r'$[\frac{\pi}{2},1]$', xycoords='data', xy=(1673523065,0.004), textcoords="offset points", xytext=(30, 30),
        #         fontsize=14, arrowprops=dict(arrowstyle='-|>', connectionstyle='angle3', color='red'))
        x_major_locator, y_major_locator = MultipleLocator(1), MultipleLocator(1)
        ax.yaxis.set_major_locator(x_major_locator), ax.yaxis.set_major_locator(y_major_locator)
        plt.plot(t_new, v, color='red',label = '')
        # plt.legend()
        plt.grid()

        plt.figure('This is the three table')
        ax = plt.gca()
        ax.spines['right'].set_color('none'),ax.spines['top'].set_color('none')
        plt.title('current_V/output_V')
        plt.xlabel('current_V'),plt.ylabel('output_V')
        x_major_locator, y_major_locator = MultipleLocator(1), MultipleLocator(1)
        ax.yaxis.set_major_locator(x_major_locator), ax.yaxis.set_major_locator(y_major_locator)
        plt.plot(current_v,ls="-", color='blue', marker='', label='current_v')
        plt.plot(output_v,ls="--", color='red', marker='', label='output_v')
        plt.legend()
        plt.grid()
        plt.show(),plt.show(),plt.show()


if __name__ == '__main__':
    csv_read_plot = CsvReadPlot(params.csv_1,params.csv_2,params.time_start,params.time_stop)
    csv_read_plot.csv_change()


