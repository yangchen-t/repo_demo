#!/bin/python3


'''写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成整个文件的批量修改操作（进阶）。'''


def file(file_name,file_content):
    f = open(file_name,'w')
    f.write(file_content)
    f.close()
file('23.csv','')