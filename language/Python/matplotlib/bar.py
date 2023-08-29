import matplotlib.pyplot as plt
import pandas as pd
import  params


csv2_file = pd.read_csv(params.csv_2)
t_1 = params.time_start
t_2 = params.time_stop
csv_2_res=csv2_file[(csv2_file["time"] > float(t_1)) & (csv2_file["time"] < float(t_2))]
current_v,output_v,speed_time = csv_2_res['current_speed'],csv_2_res['output_speed'],csv_2_res['time']
x_data = list(range(len(current_v)))
y_data = [58000, 60200, 63000, 71000, 84000, 90500, 107000]
y_data2 = [52000, 54200, 51500, 58300, 56800, 59500, 62700]
current_v = list(current_v)
# x表示起始位置
# print(current_v)
plt.bar(x=x_data, height=current_v)
# plt.bar(x=x_data, height=y_data2)
# plt.grid()
# plt.show()