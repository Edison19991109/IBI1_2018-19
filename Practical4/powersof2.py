# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:03:13 2019

@author: KANG Jianning
"""

# use the for-loop for n in (1,13)
# compare 2**n from 2**13 to 2**0 with the number
# if it's smaller 
a=14
y='2019 is ' 
for n in range (0,14):
    a=a-1
    if a==0:
        y=y+'2**0'
        break
    y=y+'2**'+str(a)+'+'
    
print (y)