# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:17:50 2019

@author: KANG Jianning
"""

import os
os.chdir(r'C:\Users\KANG Jianning\Documents\GitKraken\IBI1_2018-19\Practical13')
def xml_to_cps():
    import os
    import xml.dom.minidom
    
    # first, convert xml to cps 
    os.system("CopasiSE.exe -i predator-prey.xml -s predator-prey.cps")
    
    # now comes the painful part. Just copy and paste this ok
    
    cpsTree = xml.dom.minidom.parse("predator-prey.cps")
    cpsCollection = cpsTree.documentElement
    
    reportFile = xml.dom.minidom.parse("report_ref.xml")
    reportLine = reportFile.documentElement
    
    tasks = cpsCollection.getElementsByTagName("Task")
    for task in tasks:
        if task.getAttribute("name")=="Time-Course":
            task.setAttribute("scheduled","true")
            task.insertBefore(reportLine,task.childNodes[0])
            break
        
    
    for taskDetails in task.childNodes:
        if taskDetails.nodeType ==1:
            if taskDetails.nodeName == "Problem":
                problem = taskDetails
                
    for param in problem.childNodes:
        if param.nodeType ==1:
            if param.getAttribute("name")=="StepNumber":
                param.setAttribute("value","200")
            if param.getAttribute("name")=="StepSize":
                param.setAttribute("value","1")
            if param.getAttribute("name")=="Duration":
                param.setAttribute("value","200")
           
            
    report18 = xml.dom.minidom.parse("report18.xml")
    report = report18.documentElement
    
    listOfReports  =  cpsCollection.getElementsByTagName("ListOfReports")[0]
    listOfReports.appendChild(report)
    
    cpsFile = open("predator-prey.cps","w", encoding='utf-8')
    cpsTree.writexml(cpsFile)
    cpsFile.close()
xml_to_cps()

os.system('CopasiSE predator-prey.cps')

variable=[]
result=[]
with open(r'modelResults.csv') as modelResults:
    lines=modelResults.readlines()
    for line in lines:
        line=line.replace('\n','')
        if line=='Time,[A],[B]':
            line=line.split(',')
            variable.append(line)
        else:
            line=line.split(',')
            result.append(line)

import numpy
result = numpy.array(result)
result = result.astype(numpy.float)

import matplotlib.pyplot as plt
plt.figure(figsize=(6,4), dpi=150)
plt.plot(result[0:200,1], label='Predator (b=0.02, d=0.4)')
plt.plot(result[0:200,2], label='Prey (b=0.1, d=0.02)')
plt.xlabel('time')
plt.ylabel('population size')
plt.title('Time course')
plt.legend()

plt.figure(figsize=(6,4), dpi=150)
plt.plot(result[0:200,1], result[0:200,2])
plt.xlabel('predator population')
plt.ylabel('prey population')
plt.title('Limit cycle')
plt.legend()

from xml.dom.minidom import parse
#Find all paratermeter attributes in that SBML file.
#Randomly pick up a number and change those attributes.
#Creat a loop for procedures above. Run it for several times.