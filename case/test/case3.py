"""ort xlwt as xl
new_book=xl.Workbook(encoding='utf-8')
new_sheet=new_book.add_sheet("第一个")
new_sheet.write(3,3,'张富豪')
new_book.save("朋友表.xls")"""