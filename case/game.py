from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.figure(figsize=(20,8) )
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
x = ['7月1日', '7月2日', '7月3日', '7月4日','7月5日', '7月6日', '7月7日', '7月8日','7月9日','7月10日', '7月11日', '7月12日', '7月13日', '7月14日','7月15日']  #数据在x轴的位置，是一个可迭代对象
y1 = [3370.48, 3895.69, 5109.03, 4353.68, 3954.21, 5346.81, 5289.11, 8275.16, 5686.16,7503.41, 5360.36, 5758.59, 4962.14, 9401.22, 5543.89]
y2 = [3097.55, 3401.15, 5525.05, 4202.49, 3797., 4972.03, 4941.97, 7440.79, 5561.71, 5888.88, 3776.57, 3990.54, 4114.41, 7612.38, 4539.72]

#数据在y轴的位置，是一个可迭代对象
#plt.plot(x, y1, label='利润金额', linewidth=3, color='snow', marker='o',
         #markerfacecolor='blue', markersize=11 )
for a, b in zip(x, y1):
    plt.text(a, b+0.05, b, ha='center', va='bottom', fontsize=18, color='blue' )
for c, d in zip(x, y2):
    plt.text(c, d+0.05, d, ha='center', va='bottom', fontsize=18,color='orange' )
plt.title('7月利润变化图')
plt.xlabel('时间')
plt.ylabel('利润 单位（元）')
#plt.legend(prop =my_font)
plt.plot(x,y1,label='收益')     #传入x和y,通过plot绘制出折线图
plt.plot(x,y2,label='支出')
plt.legend()
plt.grid()
plt.show()   #展示图形

#plt.savefig("7月数据利润变化.png")
