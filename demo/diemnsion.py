#/usr/bin/env python3

'''
Used to calculate the distance between two and three points
'''

data = input("依次输入x,y,z : ")

class Compute():
    def __init__(self,all):
        self.all = all

    def diemnsion_two(self):
        x0, y0, x1, y1 = self.all[0], self.all[1],\
                         self.all[2], self.all[3]
        r = pow(pow(float(x1) - float(x0), 2) +\
                pow(float(y1) - float(y0), 2), 0.5)
        print("结果为 {:.2f}".format(r))

    def diemnsion_three(self):
        x0, y0, z0, x1, y1, z1 = self.all[0], self.all[1], self.all[2],\
                                 self.all[3], self.all[4], self.all[5]
        r = pow(pow(float(x1) - float(x0), 2) + \
                pow(float(y1)- float(y0), 2) + pow(float(z1) - float(z0), 2), 0.5)
        print("结果为 {:.2f}".format(r))

if __name__ == "__main__":
    data_change = data.split()
    compute = Compute(data_change)

    if len(data_change) == int(4):
        compute.diemnsion_two()
    elif len(data_change) == int(6):
        compute.diemnsion_three()
    else:
        print('Please enter the correct parameters!!')


