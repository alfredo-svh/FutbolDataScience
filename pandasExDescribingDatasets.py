# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:19:30 2020

@author: Alfredo
"""

import numpy as np
import pandas as pd

df = pd.read_csv("2008-09Refs.csv")
df.columns = ['Date','HomeTeam','AwayTeam',
                 'Referee','HomeFouls','AwayFouls',
                 'TotalFouls','HomeYellows','AwayYellows',
                'TotalYellows', 'HomeReds','AwayReds','TotalReds']
ds = df.describe()

groupedRefs = df.groupby("Referee")
dsRefs = groupedRefs.describe()

groupedRefs.describe()['TotalYellows']
df[df['TotalYellows']==9]
df[df['TotalFouls']==42]