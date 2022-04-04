#!/usr/bin/env python3

'''
Design login and new account application
'''
import time


data = {"username":"zhangfuhao","passwd":"123456"}

def log_in():

    for i in data.values():
        if passwd == i:
            print("Login successful!!")
        else:
            pass


def register():

    print("username or passwd not available !!")
    print("Please create a username first !")
    number = input("please enter numbers '1' create username ~ :")

    if int(number) == int(1):
        new_user = input('Please enter the new user name you want to create :')
        data["username_1"] = new_user
    else:
        print("There is an error in your input. Please enter the number 1 as prompted")

    while True :
        new_passwd = input("Please set your password : ")
        again_passwd = input("Please confirm your password again :")
        if new_passwd != again_passwd:
            print("The password setting is invalid. The two passwords are different!!")
            print("Please reset !!!")
        else:
            data["passwd_1"] = new_passwd
            print("Created successfully")
            time.sleep(3)
            break

    choice = input("Enter 1 to log in again and enter 2 to exit :")
    if int(choice) == 1 :
        print("Just a moment, please. We're jumping")
        time.sleep(2)
        user = input("plsease enter yuor username ~ :")
        passwd = input("please enter your passwd ~ :")
        log_in()
    elif int(choice) == 2 :
        exit(1)


if  __name__ == "__main__":
    user = input("plsease enter yuor username ~ :")
    passwd = input("please enter your passwd ~ :")

    if user in data.values():
        log_in()
    else:
        register()



