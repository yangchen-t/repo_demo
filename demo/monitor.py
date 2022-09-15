#!/usr/bin/env python3 

import os
from pickle import TRUE 
import time as t

# sorted(list_test, key=str.lower) 
while TRUE:
      current = sorted(os.listdir("/home/westwell/Desktop"),key=str.lower)
      print(current)
      print("cu")
      while True :
            t.sleep(10)
            new_dir_list = sorted(os.listdir("/home/westwell/Desktop"),key=str.lower)
            print(new_dir_list)
            print("new")
            if len(current) < len(new_dir_list):
                  # print(new_dir_list[-1])
                  diff = set(new_dir_list).difference(set(current))
                  for i in diff:
                        print(i)
                  break
            else:
                  print("no diff")
                  break