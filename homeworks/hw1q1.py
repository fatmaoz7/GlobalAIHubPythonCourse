# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:57:45 2021

@author: fatma oz
"""

mylist=[0,1,2,3,4,5,6,7,8,9] # created list
length=len(mylist)
mid_index=length//2 #found the mid index to separate into two
final=[] #created empty list
first_half=mylist[:mid_index];
second_half=mylist[mid_index:];
final.extend(second_half) #extending empty list with new style
final.extend(first_half)
print(final)