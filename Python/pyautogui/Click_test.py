#!/bin/python3

import pyautogui as auto
import time as t 

# 启用自动防故障功能，左上角的坐标为（0，0），将鼠标移到屏幕的左上角，来抛出failSafeException异常
auto.FAILSAFE = True  

LOGIN_USER = ""             # 登录用户名
LOGIN_PASSWD = ""           # 登录密码
TIMES = 1                   # 循环次数
Duration = 0.5              # 每个指令完成时间    设置为None 为无限循环
COUNT = 0                   # 统计次数

def Test_login_durable():
    auto.doubleClick(x=100, y=150, button="left")   # 打开 可执行文件
    auto.moveTo(100, 100, duration=Duration)        # 移动到三个点
    auto.click(x=100, y=200, duration=Duration)     # 点击登入选项
    t.sleep(1)
    auto.moveTo(100, 100, duration=Duration)        # 移动到账号输入窗口
    auto.click()                                    # 鼠标单击
    auto.typewrite(LOGIN_USER, interval=0.5)        # 输入登录用户名 
    t.sleep(1)
    auto.moveTo(100, 100, duration=Duration)        # 移动到密码输入窗口
    auto.click()                                    # 鼠标单击
    auto.typewrite(LOGIN_PASSWD, interval=0.5)      # 输入登录密码
    auto.click(x=100, y=200, duration=Duration)     # 移动到登录按钮并点击

def Exit():
    auto.moveTo(100, 100, duration=Duration)        # 移动到三个点  
    auto.click(x=100, y=200, duration=Duration)     # 点击退出选项  
    t.sleep(1)
    auto.moveTo(100, 100, duration=Duration)        # 移动到账号输入窗口
    auto.click()                                    # 鼠标单击
    auto.typewrite(LOGIN_USER, interval=0.5)        # 输入用户名
    t.sleep(1) 
    auto.moveTo(100, 100, duration=Duration)        # 移动到密码输入窗口
    auto.click()                                    # 鼠标单击
    auto.typewrite(LOGIN_PASSWD, interval=0.5)      # 输入登入密码
    auto.click(x=100, y=200, duration=Duration)     # 移动到退出按钮并点击


def main():
    if (TIMES == ""):
        print("设置循环次数")
        exit(-1)
    if (TIMES == None):
        while True:
            Test_login_durable()
            t.sleep(1)
            Exit()
            COUNT += 1
            with open("test.txt","w+") as f:
                print(COUNT,file=f)
                f.close()
    for i in range(TIMES):
        Test_login_durable()
        t.sleep(1)
        Exit()
        COUNT += 1 
        with open("test.log","w+") as f:
            print(COUNT,file=f)
            f.close()

if __name__ == '__main__':
    main()
