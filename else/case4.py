# from xlrd import open_workbook as open
# from xlutils.copy import copy as copy
# new=open(r"C:\Users\ASUS\Desktop\新建文件夹.xls")
# # print(new)
# new_copy=copy(new)
# nwe=new_copy.add_sheet("身材表")
# nwe.write(0,0,"我是你爹")
# wen=new_copy.get_sheet(1)
# new_copy.save(r"C:\Users\ASUS\Desktop\新建文件夹.xls")
# print(wen)



# import xlwt
# # for ns in range(1,2):
# nw=xlwt.Workbook(encoding='utf-8')
# add=nw.add_sheet("统计表")
# for x in range(1, 10):
#     for y in range(1,x+1):
#           # print(x,n)
#         add.write(x-1,y-1,"%dx%d=%d"%(x,y,x*y))  # \t占位符
#         # print("")
# nw.save("乘法表.xls")



# import xlwt,xlrd
# # nw=xlrd.open_workbook(r"C:\Users\ASUS\Desktop\新建文件夹.xls")
# # ns=xlwt.Workbook(encoding='utf-8')
# # ns1=ns.add_sheet("统计")
# # n=0
# # while n < nw.sheets().__len__():
# #     ns1.write(n,0,"第%d的sheet"%(n+1))
# #     ns1.write(n,1,nw.sheets()[n].name)
# #     n+=1
# # ns.save("统计结果1.xls-")



# import xlwt,xlrd
# x=1
# biao=xlwt.Workbook(encoding="utf-8")
# # sheet1=biao.add_sheet("sheet")
# for n in range(2015,2019):
#     while x<13:
#         sheet1 = biao.add_sheet("%d月份"%x)
#         x+=1
#     # print(n)
#     biao.save("%d年份报表.xls"%n)



