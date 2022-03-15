
data = input("依次输入x,y,z :")

all = data.split()
x0,y0,z0,x1,y1,z1 = all[0],all[1],all[2],all[3],all[4],all[5]

r = pow(pow(float(x1)-float(x0),2) + pow(float(y1)-float(y0),2) + pow(float(z1)-float(z0),2),0.5)
print("结果为 {:.2f}" .format(r))
