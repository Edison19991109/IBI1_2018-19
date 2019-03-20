# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:33:23 2019

@author: KANG Jianning
"""


a=input('Give me a string of words:')
# We can reverse the order of string by using indexing before it is turned to be a list.
a= a[::-1]
a = a.split(' ')
# 'reverse' doesn't include the function of 'sort', so it just reverse the order of list now.
a.sort()
a.reverse()
print(a)