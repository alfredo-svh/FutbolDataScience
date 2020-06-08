# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:09:38 2020

@author: Alfredo
"""

import pandas as pd
import numpy as np

def findWinner(val):
    if val>0:
        return "Home win"
    elif val<0:
        return "Away win"
    else:
        return "Draw"
    
    
df = pd.read_csv('2008-09Results.csv')
teams = df['HomeTeam'].unique()
df.columns

del df['Referee']

df['Result'] = df['FTHG'] - df['FTAG']
df['ResultText'] = df['Result'].apply(findWinner)

print(df['FTHG'].mean())
print(df['FTAG'].mean())

df.groupby('ResultText').mean()

df['TotalGoals'] = df['FTHG'] + df['FTAG']

df.groupby('HomeTeam').mean()['TotalGoals'].sort_values(ascending=False)
df.groupby('AwayTeam').mean()['TotalGoals'].sort_values(ascending=False)