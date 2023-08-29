import sys

import matplotlib.font_manager as f
import matplotlib.pyplot as  plt
import sys,random



fig = plt.figure(figsize=(18,10),dpi=80)
# my_font = f.FontProperties(fname=sys.argv[1])           ##字体

x = range(1,10)
y = [random.randint(20,35) for i in range(1,10)]

_x = ('这是{}'.format(i) for i in x )


plt.xticks(x,_x,rotation=45)
# plt.savefig('./demo.png')
plt.plot(x,y)
plt.savefig('./demo.png')
plt.show()
