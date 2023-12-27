rows = int(input('请输入菱形边长:'))
row = 1
while row <= rows:
    col = 1     # 保证每次内循环col都从1开始，打印前面空格的个数
    while col <= (rows-row):  # 这个内层while就是单纯打印空格
        print(' ', end='')  # 空格的打印不换行
        col += 1
    print(row * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
    row += 1
bottom = rows-1
while bottom > 0:
    col = 1     # 保证每次内循环col都从1开始，打印前面空格的个数
    while bottom+col <= rows:
        print(' ', end='')  # 空格的打印不换行
        col += 1
    print(bottom * '* ')  # 每一行打印完空格后，接着在同一行打印星星，星星个数与行数相等，且打印完星星后print默认换行
    bottom -= 1