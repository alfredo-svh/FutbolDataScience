# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:30:15 2020

@author: Alfredo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


table = pd.read_csv("EPL2016-17table.csv")
teamColors = ['#034694','#001C58','#5CBFEB','#D00027',
              '#EF0107','#DA020E','#274488','#ED1A3B',
               '#000000','#091453','#60223B','#0053A0',
               '#E03A3E','#1B458F','#000000','#53162f',
               '#FBEE23','#EF6610','#C92520','#BA1F1A']


#simple bar chart
plt.bar(x=np.arange(1,21), height =table['Pts'], color= teamColors)
plt.title("Premier League 16/17")
plt.xticks(np.arange(1,21), table['Team'], rotation=90)
plt.xlabel("Team")
plt.ylabel("Points")
plt.show()


#lollipop bar chart
plt.hlines(y=np.arange(1,21),xmin=0,xmax=table['Pts'],color=teamColors)
plt.title("Premier League 16/17")
plt.yticks(np.arange(1,21), table['Team'])
plt.ylabel("Team")
plt.xlabel("Points")
plt.plot(table['Pts'], np.arange(1,21), "o")
plt.show()


#scatter plot & crosshairs
fig, ax = plt.subplots()
fig.set_size_inches(7, 5)
ax.set_title("Goals for & Against")
ax.set_xlabel("Goals For")
ax.set_ylabel("Goals Against")
ax.text(18,90,"Poor attack, poor defense",color="red",size="8")
ax.text(67,20,"Strong attack, strong defense",color="red",size="8")
plt.plot(table['GF'],table['GA'],"o")
plt.plot([table['GF'].mean(),table['GF'].mean()],[90,20], 'k-', linestyle = ":", lw=1)
plt.plot([20,90],[table['GA'].mean(),table['GA'].mean()], 'k-', linestyle = ":", lw=1)
ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=".3")
plt.show()


#PieCharts
leagueWins = {'Team':['Manchester United','Blackburn Rovers','Arsenal',
                     'Chelsea','Manchester City','Leicester City'],
             'Championships':[13,1,3,4,2,1]}
df = pd.DataFrame(leagueWins, columns=['Team','Championships'])
teamColors=['#f40206','#0560b5','#ce0000','#1125ff','#28cdff','#091ebc']
plt.pie(df['Championships'], labels=df['Team'], colors=teamColors, startangle=90)
plt.title("Premier League Titles")
plt.tight_layout()