#/usr/bin/env python3

'''
Enter the perimeter and area of the trilateral calculation
'''



lane1 = float(input('请依次输入三角形的三边：'))
lane2 = float(input('请依次输入三角形的三边：'))
lane3 = float(input('请依次输入三角形的三边：'))

if lane1 + lane2 > lane3 and lane1 + lane3 > lane2 and lane2 + lane3 > lane1:
    perimeter = lane1 + lane2 + lane3
    s = perimeter /2
    area = (s*(s-lane1)*(s-lane2)*(s-lane3)) ** 0.5
    print('周长为{0}'.format(perimeter))
    print('面积为{0}'.format(area))
else:
    print('error,请输入正确的三边。。。')



