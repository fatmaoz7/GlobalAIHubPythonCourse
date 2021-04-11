# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:26:49 2021

@author: fatma oz
"""
dict_login={"fatmaoz": '1234', 'aliveli': '5678', 'global':'aihub'}

username1=input("Please enter your username ")
password1=input("Please enter your password ")

while username1 in dict_login.keys():
    if password1==dict_login[username1]:
        print("Successful login")
        break
    else:
        print("You should try again")
        break
else:
    print("Person does not exist")

                         
        