
data = input("依次输入x,y :")

all = data.split()
x0,y0,x1,y1 = all[0],all[1],all[2],all[3]

r = pow(pow(float(x1)-float(x0),2) + pow(float(y1)-float(y0),2),0.5)
print("结果为 {:.2f}" .format(r))
