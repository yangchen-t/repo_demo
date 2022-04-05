#!/bin/python
# import xlrd
# # yuwen=int(input("请输入你的语文成绩："))
# # shuxue=int(input("请输入你的数学成绩："))
# # yingyu=int(input("请输入你的英语成绩："))
# from case.test.case2 import books
#
# wode=xlrd.open_workbook(r"C:\Users\ASUS\Desktop\新建文件夹.xls")
# y=books.nrows   #读取excel列表的列号
# x=books.ncols   #读取excel列表的行号
# # y1_data=books.row_values(0)
# y_data=books.row_values(3)
# # yuwenchengji=books.col_values(3)
# print(y_data)
from xlrd import open_workbook as open

yuwen=int(input("请输入你的语文成绩："))
shuxue=int(input("请输入你的数学成绩："))
yingyu=int(input("请输入你的英语成绩："))
books=open(r"C:\Users\ASUS\Desktop\新建文件夹.xls").sheet_by_index(0)
y=books.nrows   #读取excel列表的列号
x=books.ncols   #读取excel列表的行号
# y1_data=books.row_values(0)
# y_data=books.row_values(3)
# cell_data_1=books.cell_value(2,2)
# cell_data_2=books.cell(2,2)
x_data=books.col_values(2)[1:]
# print(x_data)
if  int(yuwen) > 100 :
    print("语文结果:good")
else :
    print("语文不合格")
if int(shuxue) > 100:
    print("数学结果:good")
else:
    print("数学不合格")
if int(yingyu) > 50:
    print("英语结果:good")
else:
    print("英语不合格")
