
import os
os.chdir("C:\\Users\\westwell\\Desktop")
fp1=open('1.txt','r',encoding='utf-8')
x=fp1.readline()
fp2=open('2.txt','w',encoding='utf-8')
while 1:
    x=fp1.readline().split()
    if len(x)==0:
        break
    for i in range(1,len(x)):
        x[i]=int(x[i])
    sum=x[1]+x[2]+x[3]
    if x[1]>=20 and x[2]>=20 and x[3]>=20 and sum>=50:
            fp2.write('%s\t%s\n'%(x[0],'优秀'))
    elif x[2]>=60 and x[3]>=60 and sum>=180:
            fp2.write('%s\t%s\n' % (x[0], '及格'))
    else:fp2.write('%s\t%s\n' % (x[0], '不及格'))
fp1.close()
fp2.close()