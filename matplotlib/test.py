from matplotlib.pyplot import MultipleLocator
import matplotlib.pyplot as plt
import random

xt = list(range(2022,2026))
yt = list (range(6000000,15000000,2000000))
x = [2022,2023,2024,2025]
y1 = [6365100,8382836.7,11040195.93,14539938.04]
for a, b in zip(x, y1):
    plt.text(a, b+0.05, b, ha='center', va='bottom', fontsize=10, color='red' )


ax = plt.gca()
plt.plot(x,y1)     #传入x和y,通过plot绘制出折线
plt.legend()
plt.xlabel('time')
plt.ylabel("profit",rotation=360)
plt.xticks(xt)
plt.yticks(y1)

plt.grid()
plt.show()