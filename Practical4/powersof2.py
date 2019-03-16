# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:03:13 2019

@author: KANG Jianning
"""

# calculate the reminder when the number is divided by 2,
# if the reminder is 0, then record down the quotient and continue the loop;
# if the reminder is 1, then record add in into the output result and record down the quotient to continue the loop.
# if the quotient equals to 1, then record it into the output result as the last number of it and then stop the loop.
# print the result by using list and reversing the order of the number in it.
a=2019
n=0
c=0
list = []
y= str(a) + ' is ' 
while a>=1:
    b=a%2
    a=a//2
    if b==0:
        n=n+1
    else: 
         list.append(n)
         n=n+1
list.reverse()
for i in list:
    if c==0:
        y=y+'2**'+str(i)
        c=c+1
    else:
        y=y+' + '+'2**'+str(i)
        c=c+1
print (y)