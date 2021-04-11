# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 22:11:54 2021

@author: fatma oz
"""

n=int(input("Please enter a single digit integer:"))
i=0
while n>9:
    n=int(input("Wrong value!Please enter a single digit integer:"))
else:
    while i<=n:
            if i%2==0:
                print(i)
            i+=1
        