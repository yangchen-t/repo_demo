import pandas as pd

df = pd.read_csv(r'1.csv',encoding='utf-8')
df.to_excel(r'E:\python_flie\case\matplotlib\1.xls',sheet_name='data')  #转换excel
# df_excel_x_y = pd.read_excel('file.xls', usecols=[4,5])
# print(df_excel_x_y)
# x=[df_excel_x_y[1]]
# print(x)



