#！/bin/env python3
from matplotlib.pyplot import MultipleLocator 
import matplotlib.pyplot as plt
import pandas as pd
import time,sys
# import csv_path


def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def datetime_timestamp(dt):
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

# def csv_plot():
    # csv_file = pd.read_csv(sys.argv[1])
csv_file = pd.read_csv(sys.argv[1])
speed_csv = pd.read_csv(sys.argv[2])
# time_1 = input('start：')
# time_2 = input('stop：')
time_1 = input(sys.argv[2])
time_2 = input(sys.argv[3])
t_1 = datetime_timestamp(time_1)
t_2 = datetime_timestamp(time_2)
    # t=csv_file["time"]
res=csv_file[(csv_file["time"] > float(t_1)) & (csv_file["time"] < float(t_2))]
x,y,v,t_new=res["x"],res["y"],res["speed(mps)"],res['time']


plt.figure('This is the first table')
ax=plt.gca()                                                    #get current axes
    # ax.spines['right'].set_color('none')
    # ax.spines['top'].set_color('none')
plt.title('X,Y-diagram ')
plt.xlabel(' X '),plt.ylabel('Y')
x_1_major_locator,y_1_major_locator = MultipleLocator(5),MultipleLocator(10)
ax.yaxis.set_major_locator(x_1_major_locator),ax.yaxis.set_major_locator(y_1_major_locator)
plt.plot(x,y,ls="--",color='blue',marker='')
plt.grid()
    # plt.legend(loc='upper right')


    #      speed-time curve
plt.figure('This is the second table')
ax=plt.gca()
ax.spines['right'].set_color('none'),ax.spines['top'].set_color('none')
plt.title('speed diagram')
plt.xlabel(' time '),plt.ylabel('V')
    # fig = plt.figure(1, facecolor='white')
    # fig.clf()
    # plt.annotate('stopcommand',(0.38, 0.04), (0.6, 0.5), va="center",  ha="center",       #tab
    #             xycoords="axes fraction", textcoords="axes fraction",
    #             bbox=dict(boxstyle="sawtooth", fc="0.8"), arrowprops=dict(arrowstyle="<-"))
    #plt.annotate(r'$[\frac{\pi}{2},1]$', xycoords='data', xy=(1673523065,0.004), textcoords="offset points", xytext=(30, 30),
    #         fontsize=14, arrowprops=dict(arrowstyle='-|>', connectionstyle='angle3', color='red'))
x_major_locator,y_major_locator=MultipleLocator(1),MultipleLocator(1)
ax.yaxis.set_major_locator(x_major_locator),ax.yaxis.set_major_locator(y_major_locator)
plt.plot(t_new,v,ls='-',marker='',color='red')
# plt.legend(loc='upper right')
plt.grid()
plt.show(),plt.show()

if  __name__ == '__main__':
    if len(sys.argv) <3:
        print('Please provide csv path. ')
    # else:
    #     csv_plot()


