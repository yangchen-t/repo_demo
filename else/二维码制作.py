from MyQR import myqr

# myqr.run(words="我是你爸爸")
myqr.run(words=''       #内容不能为中文
            ,version=9,      #生成二维码大小
picture=r'C:\Users\ASUS\Desktop\壁纸.jpg',   #背景
         colorized=True)            #背景颜色
