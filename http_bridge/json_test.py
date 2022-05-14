#!/usr/bin/env python3 


##finish 
import json

a = '{"name":"chenxiangyang","status":False}'
try:
    data = json.loads(a)
except json.decoder.JSONDecodeError:
# print(data)
    print(1 + 1 )

for i in range(10):
    print(i)