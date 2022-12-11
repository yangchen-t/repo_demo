#!/usr/bin/env python3 

def ten_conversion()
    list1=['A','B','C','D','E','F']
    while True:
        x=int(input('请输入一个十进制数：'))
        y=x
        p=''
        q=''
        while x>0:
            m=x%2
            x//=2
            p=str(m)+p
        print('该数的二进制为：',p)
        while y>0:
            n=y%16
            i=y%16
            y = y // 16
            while i>=16:
                i=y//16
            else:
                if i<16 and i>=10:
                    n=list1[i-10]
            q=str(n)+q
        print('该数的十六进制为：',q)

def two_converiosn()
    list1=['A','B','C','D','E','F']
    while True:
        num=input('请输入一个二进制数:')
        q=''
        lenth=len(num)
        sum2=0
        for i in range(lenth):
            n=num[-i-1]
            if n!='0':
                sum1=2**i
                sum2=sum1+sum2
        print('该数的十进制为',sum2)
        y=sum2
        while y>0:
            n=y%16
            i=y%16
            y = y // 16
            while i>=16:
                i=y//16
            else:
                if i<16 and i>=10:
                    n=list1[i-10]
            q=str(n)+q
        print('该数的十六进制为：',q)

def sixteen_conversion()
    dict1={'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    while True:
        x=input('请输入一个十六进制数：')
        lenth=len(x)
        sum2=0
        for i in range(lenth):
            n=x[-i-1]
            if 'A'<=n<='F':
                num=dict1[n]
                sum1=num*16**i
                sum2+=sum1
            else:
                if n!='0':
                    sum1=int(n)*16**i
                    sum2+=sum1
        print('该数的十进制数为：',sum2)
        x=int(sum2)
        p=''
        while x>0:
            m=x%2
            x//=2
            p=str(m)+p
        print('该数的二进制为：',p)


if __name__ == "__main__":
    print("选择转换的进制：2/10/16")
    mode = input(":")
    if mode == "2": 
        two_converiosn 
    elif mode == "10":
        ten_conversion
    elif mode == "16":
        sixteen_conversion
    else 
        print("error mode ,please try again !")
