# -*- coding: utf-8 -*-
"""
Created on Wed Mar 20 09:09:37 2019

@author: KANG Jianning
"""

a= input('Give me a sequence of DNA:')
b= list(a)
myDict={}
for word in a:
    if word in ['A', 'T', 'G', 'C']:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
myDict
print (myDict)
        

import matplotlib.pyplot as plt
labels = myDict.keys()
sizes = myDict.values()
explode = [0]*len(labels) 

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  
plt.title('pie of the four DNA nucleotides')
plt.show()


#labels = myDict.keys()
#sizes = myDict.values()