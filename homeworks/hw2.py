# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:26:49 2021

@author: fatma oz
"""
dict_login={"fatmaoz": '1234', 'aliveli': '5678', 'global':'aihub'}

username1=input("Please enter your username ") #getting input from user
password1=input("Please enter your password ")

while username1 in dict_login.keys():
    if password1==dict_login[username1]: #checking if input and name are same
        print("Successful login")
        break
    else:
        print("You should try again") # if not same, getting error
        break
else:
    print("Person does not exist") # otherwise, person do not exist in that dictionary

                         
        