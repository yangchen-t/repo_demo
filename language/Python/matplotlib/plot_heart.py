import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,121)

# plt.plot(np.cos(x),np.sin(x))
# plt.plot(np.cos(x)/2,np.sin(x)/3)

plt.plot(np.cos(x)*(1-np.sin(x))/2,np.sin(x)*(1-np.sin(x))/2)
# plt.grid()
plt.axis([-1.3,1.3,-1,1])
plt.legend(['heart'])

plt.show()
