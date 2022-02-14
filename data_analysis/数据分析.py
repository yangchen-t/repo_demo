import pandas as pd
import csv

for i in range(1,178):
 url = 'https://s.askci.com/data/quarterindustry/' % (str(i))
 tb = pd.read_html(url)[3]
 tb.to_csv(r'2.csv', mode='a', encoding='utf_8_sig', header=1, index=0)
 print('第'+str(i)+'页抓取完成')
 # 'http://s.askci.com/stock/a/?reportTime=2017-12-31&pageNum=%s