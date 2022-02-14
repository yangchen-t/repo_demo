'''from matplotlib import pyplot as plt
from Global_List import *
import math
import numpy as np
from matplotlib.pyplot import MultipleLocator

# Global_List文件中定义了一些参数的值


v_sh = 2
a = -3.03493352192820e-10
b = 0.0551645264442086
c = 1.33453140871192
# 画子图是为了legend显示完全
fig, ax = plt.subplots()

for v in range(11):
    RHO = []
    Q = []
    visorAngle = 0.1 * v
    for i in range(10, 61):
        q = i / 10 * 3600
        Q.append(q)
        rho_i = visorAngle * (a * math.pow(q, 2) + b * v_sh + c) + (1 - visorAngle) * rhoWater
        RHO.append(rho_i)
    plt.plot(Q, RHO)

# 自定义X轴的刻度显示值
X_ticks = np.arange(3600, 25200, 3600)
plt.xticks(X_ticks, [i for i in range(1, 7, 1)])
# 设置X轴的刻度显示，以下为 显示3600的倍数的数值，该数值是原始横坐标值，并非自定义的刻度值
x_major_locator = MultipleLocator(3600)
ax.xaxis.set_major_locator(x_major_locator)
plt.xlabel("Flow m³/s")
plt.ylabel("Density  *10³kg/m³")
# 定义legend在图像外
plt.show()
lgnd = plt.legend(
    ["VA=0.0", "VA=0.1", "VA=0.2", "VA=0.3", "VA=0.4", "VA=0.5", "VA=0.6", "VA=0.7", "VA=0.8", "VA=0.9", "VA=1.0"],
    bbox_to_anchor=(1.05, 1), loc=2)
# 通过画子图的方式，使legend显示完全，如果不用这种方法，legend放在图像外面时，legend显示不全
fig.subplots_adjust(right=0.75)

'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6]
y = [3, 4, 5, 6, 7, 8]

plt.plot(x,y,'ro',ls='-')
plt.plot(x[0],y[0],'g *')

plt.show()