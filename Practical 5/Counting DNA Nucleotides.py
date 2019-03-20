# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:09:37 2019

@author: KANG Jianning
"""

a= input('Give me a sequence of DNA:')
b=0
c=0
d=0
e=0
for char in a:
    if char == 'A' :
        b += 1
    if char == 'C':
        c += 1
    if char == 'G' :
        d += 1
    if char == 'T' :
        e += 1
print ("A':", b,',',"'C':", c,',',"'G':", d,',',"'T':", e,'.')

import matplotlib.pyplot as plt
labels = 'A', 'C', 'G', 'T'
sizes = [b, c, d, e]
explode = (0, 0.1, 0, 0) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.title('pie of the four DNA nucleotides')
plt.show()