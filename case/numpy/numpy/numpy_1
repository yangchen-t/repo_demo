row = int(input('请输入你想输入的菱形行数，必须为奇数'))
last_kong  = int((row + 1) / 2 ) +1             #5
last_star = int((row + 1) / 2 ) +1                #5
if  row  %   2   ==  0   :                                          
    while   True :
            row = int(input('请重新输入，不为奇数'))
            if   row %    2   ==  1:                                                                    
                print('输入成功')
                break                                                           
for     i   in  range(1,row +   1):                         #1,8=1,2,3,4,5,6,7
    if  (i  ==  int((row + 1)    /   2   ))     or      (  i   >  int((row  +    1)/   2)) :                  #  1 == 4     or       1 >  4
        last_kong   =   last_kong   -   1                                                                                   # 5 = 5 -1              
        last_star   =      last_star    -   1                                                                                     #5 = 5-1
    if  i       <   int((row    +   1)  /   2   ):                                                                                    #1 <  4
        for komgge  in  range(i ,   int((row -   1)/ 2+1)):                                                     #    range(1,2)        1   
            print('  ',end=' ')                                                                                                            #'',end=''                               
        for star in range(i *   2   -   1):                                                                                         
            print(' * ',end=' ')
    else:
        for komgge  in  range(int((row   +   1  )/   2)  -   last_kong):
                print(' ',end=' ')
        for star in range(last_star   *  2   -  1):
                print(' * ',end=' ')
    print()