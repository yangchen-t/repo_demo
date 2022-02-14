import xlwt,xlrd
import xlutils as xl

'''workbook = xlwt.Workbook()
sheet1 = workbook.add_sheet('sheet1',cell_overwrite_ok=True)
sheet2 = workbook.add_sheet('sheet2',cell_overwrite_ok=True)
#
sheet1.write(0,0,'this should overwrite1')
sheet1.write(0,1,'aaaaaaaaaaaa')
sheet2.write(0,0,'this should overwrite2')
sheet2.write(1,2,'bbbbbbbbbbbbb')
workbook.save('2.xls')'''

read_file = xlrd.open_workbook('2.xls')
workbook_sheet1 = read_file.sheet_by_name(u"sheet1")
names = read_file.sheet_names()
num_rows = workbook_sheet1.nrows
num_cols = workbook_sheet1.ncols
for rown in range(num_rows):
    for coln in range(num_cols):
        cell = workbook_sheet1.cell_value(rown,coln)
        print(cell)
# print(workbook_sheet1)
# print(names)
