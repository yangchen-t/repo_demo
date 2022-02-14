number=input("请输入你的工号：")
time=int(input("请输入你的工时："))
money=int(input("请输入工资单价"))

if time >= int(120):
    number_money1=time*money + ((time-120)*1.2)
#    number_money=number_money2 + number_money1
    print(number_money1)
elif time < int(60) :
    TIME_MONEY=(int(time*money)-700)
    print(TIME_MONEY)
else :
    min_money=(time*84)
    print(min_money)