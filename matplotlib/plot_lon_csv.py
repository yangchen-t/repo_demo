import matplotlib.pyplot as plt
import pandas as pd
import  time,sys

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt

def datetime_timestamp(dt):
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)

def csv_plot():
    csv_file = pd.read_csv('lon_log_2021-12-21_180611.csv')
    # time_1 = input('start：')
    # time_2 = input('stop：')
    # t_1 = datetime_timestamp(input('start：'))
    # t_2 = datetime_timestamp(input('stop：'))
    t_1 = ('1640136039')
    t_2 = ('1640136050')
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.figure(figsize=(10,6))
    plt.rcParams['axes.unicode_minus'] = False
    new_file = csv_file[(csv_file['time'] > float(t_1)) & (csv_file['time'] < float(t_2))]
    time,current,output= new_file['time'],new_file['current_v'],new_file['output_v']
    speed_less = current[(current < float(0))]
    for a, b in zip(time, speed_less):
        plt.text(a, b + 0.05, b, ha='center', va='bottom', fontsize=18, color='blue')
    # for c, d in zip(time, output):
    #     plt.text(c, d + 0.05, d, ha='center', va='bottom', fontsize=18, color='orange')
    plt.plot(time,current,label='current_v')
    plt.plot(time,output,label='output_v')
    plt.title('speed_contrast')
    plt.xlabel('time'),plt.ylabel('speed')
    plt.legend()
    plt.grid()
    plt.show(),plt.show()

if  __name__ == '__main__':
    if len(sys.argv) <0:
        print('Please provide csv path. ')
    else:
         csv_plot()

