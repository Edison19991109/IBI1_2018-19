# -*- coding: utf-8 -*-
"""
Created on Sun May 12 18:45:18 2019

@author: KANG Jianning
"""

#Import necessary libraries.
import numpy as np
import matplotlib.pyplot as plt

#Define a function of plotting hotmap.
def drawhotmap(i, population):
    if i in [1, 10, 50, 100]:
        plt.figure(figsize=(6,4), dpi=150)
        plt.imshow(population, cmap='viridis', interpolation='nearest')

#Make array of all susceptible population.
population=np.zeros((100,100))

#Choose one random point for where the outbreak happen.
outbreak = np.random.choice(range(100),2)
population[outbreak[0], outbreak[1]] = 1

#First, count the times of loop.
#Secondly, find out all infected points.
#Thirdly, determine whether neighbours of singly infected points have been infected or not.
#Forthly, randomly decide whether it get infected or not.
#Finally, randomly decide whehter repsective infected points get recovered or not.

beta=0.3; gamma=0.05
#i counts the times of loop.
for i in range(1,101):
    #Draw hot map in specific timepoints.
    drawhotmap(i, population)
    #Find out all infected points.
    infected=np.where(population==1)
    #List all neighbours of each infected points by using a loop.
    for j in range(len(infected[0])):
        x=infected[0][j]
        y=infected[1][j]
        for xNeighbour in range(x-1,x+2):
            for yNeighbour in range(y-1,y+2):
                #Determine whether it is the infected point itself.
                if (xNeighbour,yNeighbour) != (x,y):
                    if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                        #Determine whether neighbours of singly infected points have been infected or not.
                        if population[xNeighbour,yNeighbour]==0:
                            #Randomly decide whether it gets infected or not.
                            population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        #Randomly decide whehter repsective infected points get recovered or not.
        population[x,y]=np.random.choice(range(1,3), 1, p=[1-gamma, gamma])[0]