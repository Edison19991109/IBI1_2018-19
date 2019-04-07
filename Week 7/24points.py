# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 09:28:16 2019

@author: KANG Jianning
"""


from operator import mul, sub, add
 
 
def div(a, b):
    if b == 0:
        return 999999.0
    return a / b
 
ops = {mul: '*', div: '/', sub: '-', add: '+'}
 
def solve(a,Num):
    if len(Num) == 1:
        if round(Num[0], 5) == round(24, 5):
          print ('Yes')
          print('Recursion time:',a)
    else:
        for i, n1 in enumerate(Num):
            for j, n2 in enumerate(Num):
                if i != j:
                    for op in ops:
                        a+=1
                        Num = [n for k, n in enumerate(Num) if k != i and k != j] + [op(n1, n2)]
                        yield from solve(a,Num)
 

numbers=input('Please input numbers to computer 24(use "," to divide them):')
Number=numbers.split(r',')
after_check=[]
for i in Number:
    after_check.append(int(i))
    if int(i)<0 or int(i)>=24:
        print ('The input number must be integers from 1 to 23.')
        break
    else:
        continue
try:
  a=0
  next(solve(a,after_check))
except StopIteration:
  print("No solution found")