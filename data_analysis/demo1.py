#!/bin/bash

import requests as req


with open('23.csv','w') as f :
    city = {'wd':'长城'}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = req.get('http://v.juhe.cn/todayOnhistory/queryEvent.php',params=city,headers=headers)
    print(response.text,file=f)