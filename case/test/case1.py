#这是开始
#!/bin/python
import xlrd
num=input("请输入你的分数：")
num1=float(num)
# print(type(num1))
num2=num1/2
num3=num1/4

num4=num1/10
print("你的分数除以二是"+"%d"%num2,"你的分数除以四是"+"%-.2f"%num3,"你的分数除以十是"+"%d"%num4)