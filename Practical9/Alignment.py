# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:18:58 2019

@author: KANG Jianning
"""


import pandas as pd
data = pd.read_csv(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\blosum62.txt', sep=r' +', engine='python')
blosum= data.to_dict()
    
human=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\Sequence_for_human_SOD2_protein_(NP_000627.2).txt')
human=human.read()
mouse=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\Sequence_of_a_mouse_SOD2_protein_(NP_038699.2).txt')
mouse=mouse.read()
random=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\A_random_sequence.txt')
random=random.read()

score1=0
compare1=[]
for i in range(len(human)):
    score1+=blosum[human[i]][mouse[i]]
    if human[i]==mouse[i]:
        compare1.append(human[i])
    elif blosum[human[i]][mouse[i]]>=0:
        compare1.append('+')
    else:
        compare1.append(' ')
compare1= ''.join(compare1)        
print (score1)
print(human)
print(compare1)
print(mouse)

score2=0
for i in range(len(human)):
    score2+=blosum[human[i]][random[i]]
print (score2)
    
score3=0
for i in range(len(mouse)):
    score3+= blosum[mouse[i]][random[i]]
print(score3)