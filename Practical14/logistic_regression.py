# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:18:25 2019

@author: KANG Jianning
"""

import pandas as pd
df= pd.read_excel('Final_Fluview_Practical_dataset.xlsx')
df_regress = df[['Virus Strain',
                 'Age',
                 'Gender',
                 'Hospitalized?',
                 'Swine Contact?',
                 'Attended Agricultural Event?']]

df_regress = df_regress.dropna()
df_regress['Age'] = df_regress['Age'].map({'<18 Years':0,
                                           '>=18 Years':1})
df_regress['Gender'] = df_regress['Gender'].map({'Male':0,
                                                 'male':0,
                                                 'Female':1,
                                                 'female':1})
df_regress['Hospitalized?'] = df_regress['Hospitalized?'].map({'Yes':1,
                                                               'yes':1,
                                                               'No':0,
                                                               'no':0})
df_regress['Swine Contact?'] = df_regress['Swine Contact?'].map({'Yes':1,
                                                                 'yes':1,
                                                                 'No':0,
                                                                 'no':0})
df_regress['Attended Agricultural Event?'] = df_regress['Attended Agricultural Event?'].map({'Yes':1,
                                                               'yes':1,
                                                               'No':0,
                                                               'no':0})
df_regress['Virus Strain'] = df_regress['Virus Strain'].map({'Influenza A H3N2v':1,
                                           'Influenza A H1N1v':0,
                                           'Influenza A H1N2v':0,
                                           'Influenza A H7N2':0})


import statsmodels.api as sm
import statsmodels.formula.api as smf
endog = df_regress['Virus Strain']
exog = df_regress[['Age',
                   'Gender',
                   'Hospitalized?',
                   'Swine Contact?',
                   'Attended Agricultural Event?']]
exog = sm.add_constant(exog)
logit = smf.Logit(endog, exog)
result = logit.fit()
print(result.summary())

import numpy as np

print('Odds ratios:')
print(np.exp(result.params))
