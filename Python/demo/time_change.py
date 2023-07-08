#!/usr/bin/env python3 

import time as t 
import subprocess as sub 
import sys

def TsChange(ts, interval, count):
    rts = int(sub.getoutput("date -d '{0}' +%s".format(ts)))
    print(rts)
    for i in range(int(count / interval)):
        rts += interval
        print(rts)


# python3 $0 "Apr 20 20:00:00 10 3600"
TsChange(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

