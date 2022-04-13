
'''
with open("04-07.txt",'r') as f:
    lines = f.readlines()

with open('04-07.txt','w') as nf:
    for i in range(len(lines)):
        lines[i] = str(i+1) + lines[1]
    nf.write(lines)
'''
'''
A = {
    "zhang": "2301",
    "zhao": "2302",
    "li": "2304",
    "sun": "2305"
}

a = input('plears index phone name ~:')

if  a in A.keys():
    print(A[a])
else:
    print('name not found')
'''

    # a = dict(d)
# print(a)


with open("04-07.txt",'a') as  f :
    # f.seek(2)
    # f.write('1920')
    f.seek(0,0)

    f.write('Blowin in zhe wind')
