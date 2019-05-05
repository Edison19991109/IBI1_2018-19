# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:18:58 2019

@author: KANG Jianning
"""

import sys
import pandas as pd
data = pd.read_csv(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\blosum62.txt', sep=r' +', engine='python')
blosum= data.to_dict()
# Read Blosum62 in pandas and change it into dictionary.
# Blosum62 reference: https://www.ncbi.nlm.nih.gov/Class/FieldGuide/BLOSUM62.txt, from NCBI.
    
human=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\Sequence_for_human_SOD2_protein_(NP_000627.2).txt')
human=human.read()
mouse=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\Sequence_of_a_mouse_SOD2_protein_(NP_038699.2).txt')
mouse=mouse.read()
random=open(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical9\A_random_sequence.txt')
random=random.read()
# Read the sequences.

def output(score, sequence1, compare, sequence2, name1, name2):
    print('This is the score comparing',name1, 'and', name2, ':', end='');print('\033[1;31;43m',end='');print(score);print('\033[0m', end=''); print()
    print(sequence1); print()
    print('\033[1;37;44m',end=''); print(compare);print('\033[0m');print()
    print(sequence2);print('*' *50)
# Define the format of output.

def compare_two_sequence(sequence1, sequence2, Name1, Name2):
    score=0
    compare=[]
    for i in range(len(sequence1)):
        score+=blosum[sequence1[i]][sequence2[i]]
        if sequence1[i]==sequence2[i]:
            compare.append(sequence1[i])
        elif blosum[sequence1[i]][sequence2[i]]>=0:
            compare.append('+')
        else:
            compare.append(' ')
    compare=''.join(compare)
    output(score, sequence1, compare, sequence2, Name1, Name2)
# Define the comparing function.

compare_two_sequence(human, mouse, 'human', 'mouse')
compare_two_sequence(human, random, 'human', 'random')
compare_two_sequence(mouse, random, 'mouse', 'random')
# Note: Based on the result, human and mouse SOD2 protein have a very similar sequence as score is up to 1091. 
# While compared random sequence with human or mouse sequence, surprisingly, scores are both a same negative interger.
# So when we want to use the score of smiliarity between two different sequence, it is better to provide a baseline.
# Comparing it with random sequence maybe a good idea.