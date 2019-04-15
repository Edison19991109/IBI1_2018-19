# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 09:55:31 2019

@author: KANG Jianning
"""

import re
from xml.dom.minidom import parse
import pandas as pd

def countchildnodes(id, ChildrenSet):
    for gene in terms:
        parent=gene.getElementsByTagName('is_a')[0].childNodes[0].data
        child=gene.getElementsByTagName('id')[0].childNodes[0].data
        for par in parent:
            if par == id:
                ChildrenSet.add(child)
                countchildnodes(child, ChildrenSet)
            

df = pd.DataFrame(columns=['id','name','definition','childnodes'])   
DomTree = parse('go_obo.xml')
terms=DomTree.documentElement.getElementsByTagName('term')
#extract the <is-a> tag, and then compare with gold term in the follwoing.
#define a function and ilteration it in the set to find a child of 
for term in terms:
    definition=term.getElementsByTagName('defstr')[0].childNodes[0].data
    if re.search('autophagosome',definition):
        id=term.getElementsByTagName('id')[0].childNodes[0].data
        name=term.getElementsByTagName('name')[0].childNodes[0].data
        ChildrenSet=set()
        countchildnodes(id, ChildrenSet)
        df = df.append(pd.DataFrame({'id':[id],'name':[name],'definition':[definition],'childnodes':[len(ChildrenSet)]}))

df.to_excel('output.xlsx',index=False)  

