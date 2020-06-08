# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:35:31 2020

@author: Alfredo
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("SP1.csv")

teams = data.HomeTeam.unique()
teamPoints = {team : [0] for team in teams}

for row in data.itertuples():
    home = row.HomeTeam
    away = row.AwayTeam
    
    if row.FTHG > row.FTAG:
        teamPoints[home].append(3+teamPoints[home][-1])
        teamPoints[away].append(teamPoints[away][-1])
    elif row.FTAG > row.FTHG:
        teamPoints[away].append(3+teamPoints[away][-1])
        teamPoints[home].append(teamPoints[home][-1])
    else:
        teamPoints[home].append(1+teamPoints[home][-1])
        teamPoints[away].append(1+teamPoints[away][-1])
    
matchday = list(range(0,39))

#barebones plot
fig, ax = plt.subplots()
#Add our data, setting colours and widths of lines
plt.plot(matchday, teamPoints["Betis"], color = "#0BB363", linewidth=2)
plt.plot(matchday, teamPoints["Celta"], color = "#8ac3ee", linewidth=2)
#Give the axes and plot a title each
plt.xlabel('Gameweek')
plt.ylabel('Points')
plt.title('Betis v Celta Running Points')
#Add a faint grey grid
plt.grid()
ax.xaxis.grid(color = "#F8F8F8")
ax.yaxis.grid(color = "#F9F9F9")
#Remove the margins between our lines and the axes
plt.margins(x=0,y=0)
#Remove the spines of the chart on the top and right sides
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)