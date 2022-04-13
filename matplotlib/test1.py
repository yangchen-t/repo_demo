import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

#绘制在同一个figure中
plt.figure()
plt.plot(x,y1)
plt.plot(x,y2,color='red',linewidth = 2.0,linestyle = '--')#指定颜色,线宽和线型

#截取x,y的某一部分
plt.xlim((-1,2))
plt.ylim((-2,3))
#设置x,y的坐标描述标签
plt.xlabel("I am x")
plt.ylabel("I am y")
#设置x刻度的间隔
new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks)
plt.yticks([-2, -1.5, 0, 1.5, 3],
           [r'$Really\ bad\ \alpha$', r'$bad$', r'$normal$', r'$good$', r'$very\ good$'])#r表示正则化,$$表示用数学字体输出

plt.show()

