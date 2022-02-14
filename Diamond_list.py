a = int(input('输入想要的行数：'))
last_kong = int((a + 1 ) / 2 ) + 1
last_star = int((a + 1 ) / 2 ) + 1
if a % 2 == 0 :
    while True:
        a = int(input('不为奇数'))
        if a % 2 == 1:
            print('succeed')
            break
for i in range(1,a + 1 ):
    if (i == int((a + 1 ) / 2 )) or (i > int(a + 1 ) / 2 ):
        last_kong -= 1
        last_star -= 1
    if i < int((a + 1 ) / 2 ):
        for kon in range(i,int((a - 1 ) / 2 + 1 )):
            print(' ',end=' ')
        for sta in range(i * 2 - 1 ):
            print('*',end=' ')
    else:
        for kon in range(int((a + 1 ) / 2 ) - last_kong):
            print(' ',end=' ')
        for sta in range(last_star * 2 - 1 ):
            print('*',end=' ')
    print()