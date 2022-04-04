#!/usr/bin/env python3

'''
USD Exchange
'''


num1 = float(input('Enter the exchange rate from dollars to RMB :'))
num2 = int(input('Enter 0 to convert dollars to RMB and 1 vice versa :'))
num3 = float(input('Enter the dollar amount :'))
if num2 == int(0) :
    data = num3 * num1
    print(data)
elif num2 == int(1):
    data = num3 / num1
    print(data)
else:
    print("I don't understand")