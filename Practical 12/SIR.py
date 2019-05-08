# -*- coding: utf-8 -*-
"""
Created on Wed May  8 09:08:19 2019

@author: KANG Jianning
"""

#Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

#Define variables and arrays.
N= 10000; beta=0.3; gamma=0.05
Susceptible=9999; Infected=1; Recovered=0
susceptible=[Susceptible]; infected=[Infected]; recovered=[Recovered]
    
# A loop runs 1000 time. So we need a variable to track the running time.
# A random function to calculate how many people are infected and recovered.
# Array to tract by timepoint.
count=0
while count <= 1000:
    count+=1
    NewInfected= sum(np.random.choice(range(2), Susceptible, p=[1-beta*Infected/N, beta*Infected/N ]))
    NewRecovered= sum(np.random.choice(range(2), Infected, p=[1-gamma, gamma]))
    Susceptible= Susceptible - NewInfected
    Infected= Infected + NewInfected - NewRecovered
    Recovered= Recovered + NewRecovered
    susceptible.append(Susceptible); infected.append(Infected); recovered.append(Recovered)
# Plot it.    
plt.figure(figsize=(6,4), dpi=150)
plt.plot(susceptible, label='susceptible')
plt.plot(infected, label='infected')
plt.plot(recovered, label= 'recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.savefig(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical 12\SIR_Figure', type='png')