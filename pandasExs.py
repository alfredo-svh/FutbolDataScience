# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 14:15:05 2020

@author: Alfredo
"""

import numpy as np
import pandas as pd

#series
Capacity = pd.Series(data=[60432,55097,39460],
                     index=["Emirates Stadium","Etihad Stadium","Elland Road"])
CapacityDict = {'Ewood Park':31367,
                'Liberty Stadium':20937,
                'Portman Road':30311}
Capacity = pd.Series(CapacityDict)
Capacity


#DataFrames
PlayerList = ["Pagbo","Grazemen","Cantay","Ravane"]
SkillList=["Shooting","Passing","Defending"]
ScoresArray = np.random.randint(1,10,(4,3))
df = pd.DataFrame(data=ScoresArray, index=PlayerList, columns=SkillList)
df['Shooting']
df.loc['Pagbo']
df.iloc[1:3]
df['Communication'] = np.random.randint(1,10,4)
df = df.drop("Defending", axis=1)
df = df.drop('Grazemen')
df.loc['Gomez'] = np.random.randint(1,10,3)
df>5
df['Shooting']>5
df[df['Shooting']>5]


#missing data
df = pd.DataFrame({'Wage':[150000,123000,np.nan],
                   'GoalBonus':[4000,np.nan,np.nan],
                   'ImageRights':[50000,70000,100000]}, 
                index=['Konda','Makho','Grey'],
                columns=['Wage','GoalBonus','ImageRights'])
#return rows with no NaNs
df.dropna()
#return columns with no NaNs
df.dropna(axis=1)
# return df dropping rows with 2 or more NaNs
df.dropna(thresh=2)
#return df filling NaNs in column with vaue = average of column
df['Wage'].fillna(value=df['Wage'].mean())


#grouping data
data = {'Opponent':
        ["Atletico Jave","Newtown FC", 
         "Bunton Town", "Fentborough Dynamo"],
       'Location':
        ["Home","Away","Away","Home"],
        'GoalsFor':
        [2,4,3,0],
        'GoalsAgainst':
        [4,0,2,2]}
Matches = pd.DataFrame(data)
Matches.groupby('Location').mean()
Matches.groupby('Location').describe().transpose()['Away']


#joining data
match1 = pd.DataFrame({'Opponent':['Selche FC'],
                      'GoalsFor':[1],
                       'GoalsAgainst':[1],
                       'Attendance':[53225]})
match2 = pd.DataFrame({'Opponent':['Sudaton FC'],
                      'GoalsFor':[3],
                       'GoalsAgainst':[0],
                       'Attendance':[53256]})
match3 = pd.DataFrame({'Opponent':['Ouestjambon United'],
                      'GoalsFor':[4],
                       'GoalsAgainst':[1],
                       'Attendance':[53225]})
AllMatches = pd.concat([match1,match2,match3])
match1scorers = pd.DataFrame({'First':['Sally'],
                              'Last':['Billy'],
                            'Opponent':['Selche FC']})
                      
match2scorers = pd.DataFrame({'First':['Sally'],
                              'Last':['Pip'],
                             'Opponent':['Sudaton FC']})

match3scorers = pd.DataFrame({'First':['Sally'],
                             'Last':['Sally'],
                             'Opponent':['Ouestjambon United']})
AllScorers = pd.concat([match1scorers,match2scorers,match3scorers]) 
pd.merge(AllMatches, AllScorers, how='inner',on='Opponent')