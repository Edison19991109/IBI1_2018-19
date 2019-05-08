# -*- coding: utf-8 -*-
"""
Created on Wed May  8 10:45:52 2019

@author: KANG Jianning
"""

#Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

def model(Susceptible, Recovered, Percentage):
    N= 10000; beta=0.3; gamma=0.05
    Infected=1
    susceptible=[Susceptible]; infected=[Infected]; recovered=[Recovered]    
    count=0
    while count <= 1000:
        count+=1
        NewInfected= sum(np.random.choice(range(2), Susceptible, p=[1-beta*Infected/N, beta*Infected/N ]))
        NewRecovered= sum(np.random.choice(range(2), Infected, p=[1-gamma, gamma]))
        Susceptible= Susceptible - NewInfected
        Infected= Infected + NewInfected - NewRecovered
        Recovered= Recovered + NewRecovered
        susceptible.append(Susceptible); infected.append(Infected); recovered.append(Recovered)
    plt.plot(infected, label=str(Percentage) + '%')
    plt.xlabel('time')
    plt.ylabel('number of people')
    plt.title('SIR Model')
    plt.legend()

for i in range(0,110,10):
    percentage=i/100
    model(int(10000-10000*percentage), int(10000*percentage), i)
#100% is an exception.