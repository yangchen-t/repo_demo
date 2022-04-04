#!/bin/python
from xlrd import open_workbook as open

books=open(r"C:\Users\ASUS\Desktop\新建文件夹.xls").sheet_by_index(0)
y=books.nrows   #读取excel列表的列号
x=books.ncols   #读取excel列表的行号
y1_data=books.row_values(0)
y_data=books.row_values(3)
# cell_data_1=books.cell_value(2,2)
# cell_data_2=books.cell(2,2)
x_data=books.col_values(3)
print(x_data)
#
# print(cell_data_2)
# print(y,x)
# sheet=book.sheets()
# sheet_name=book.sheet_names()
# wps1=book.sheet_by_name("第一个")
# wps2=book.sheet_by_index(0)
# wps3=book.sheets()[1]
# print(book,sheet)
# print(sheet_name,wps1)
# print(wps2.name)
# print(wps3)
