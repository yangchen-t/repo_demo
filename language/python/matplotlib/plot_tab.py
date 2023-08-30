import matplotlib.pyplot as plt
import pandas as pd

csv_file=pd.read_csv("task_log_2021-11-16_120135.csv")
t1=1637121285
t2=1637121683

t=csv_file["time"]
res=csv_file[(csv_file["time"] > float(t1)) & (csv_file["time"] < float(t2))]
x,y,v,t_new=res["x"],res["y"],res["speed(mps)"],res['time']
# plt.figure('This is the second table')
ax=plt.gca()
ax.spines['right'].set_color('none'),ax.spines['top'].set_color('none')


fig = plt.figure(1, facecolor='white')
fig.clf()
plt.annotate('stopcommand:0/time:1637121432',(0.38, 0.04), (0.6, 0.5), va="center",  ha="center",
                 xycoords="axes fraction", textcoords="axes fraction",color='r',
                 bbox=dict(boxstyle="sawtooth", fc="0.8"), arrowprops=dict(arrowstyle="<-",color='r'))

plt.annotate('missioncommand:5/time:1637121401',(0.315, 0.04), (0.4, 0.8), va="center",  ha="center",
                 xycoords="axes fraction", textcoords="axes fraction",
                 bbox=dict(boxstyle="sawtooth", fc="0.8"), arrowprops=dict(arrowstyle="<-"))
plt.title('speed diagram')
plt.xlabel(' time '),plt.ylabel('V')


plt.plot(t_new,v,ls='-',marker='')
plt.grid()
plt.show()
