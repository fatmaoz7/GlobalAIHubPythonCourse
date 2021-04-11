# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:57:45 2021

@author: fatma oz
"""

mylist=[0,1,2,3,4,5,6,7,8,9]
length=len(mylist)
mid_index=length//2
final=[]
first_half=mylist[:mid_index];
second_half=mylist[mid_index:];
final.extend(second_half)
final.extend(first_half)
print(final)