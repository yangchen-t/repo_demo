#!/usr/bin/env python3

foo = [2,18,9,22,17,24,8,12,27]

def filtered():
    for n in foo:
        if n % 3 == 0 :
            print(n)

filtered()

