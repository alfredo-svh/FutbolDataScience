# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:51:21 2020

@author: Alfredo
"""

from scipy.spatial import ConvexHull
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def createPitch():
    
    #Create figure
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)

    #Pitch Outline & Centre Line
    plt.plot([0,0],[0,90], color="black")
    plt.plot([0,130],[90,90], color="black")
    plt.plot([130,130],[90,0], color="black")
    plt.plot([130,0],[0,0], color="black")
    plt.plot([65,65],[0,90], color="black")
    
    #Left Penalty Area
    plt.plot([16.5,16.5],[65,25],color="black")
    plt.plot([0,16.5],[65,65],color="black")
    plt.plot([16.5,0],[25,25],color="black")
    
    #Right Penalty Area
    plt.plot([130,113.5],[65,65],color="black")
    plt.plot([113.5,113.5],[65,25],color="black")
    plt.plot([113.5,130],[25,25],color="black")
    
    #Left 6-yard Box
    plt.plot([0,5.5],[54,54],color="black")
    plt.plot([5.5,5.5],[54,36],color="black")
    plt.plot([5.5,0.5],[36,36],color="black")
    
    #Right 6-yard Box
    plt.plot([130,124.5],[54,54],color="black")
    plt.plot([124.5,124.5],[54,36],color="black")
    plt.plot([124.5,130],[36,36],color="black")
    
    #Prepare Circles
    centreCircle = plt.Circle((65,45),9.15,color="black",fill=False)
    centreSpot = plt.Circle((65,45),0.8,color="black")
    leftPenSpot = plt.Circle((11,45),0.8,color="black")
    rightPenSpot = plt.Circle((119,45),0.8,color="black")
    
    #Draw Circles
    ax.add_patch(centreCircle)
    ax.add_patch(centreSpot)
    ax.add_patch(leftPenSpot)
    ax.add_patch(rightPenSpot)
    
    #Prepare Arcs
    leftArc = Arc((11,45),height=18.3,width=18.3,angle=0,theta1=310,theta2=50,color="black")
    rightArc = Arc((119,45),height=18.3,width=18.3,angle=0,theta1=130,theta2=230,color="black")

    #Draw Arcs
    ax.add_patch(leftArc)
    ax.add_patch(rightArc)
    
    #Tidy Axes
    plt.axis('off')


df = pd.read_json("events_World_Cup.json")
columns = ["eventName", "eventSec", "matchId", "matchPeriod", "playerId", "teamId","xstart", "ystart","xend", "yend"]
#exclude irrelevant rows
df.drop(df[df['matchId'] != 2057954].index, inplace = True)
df.drop(df[df['playerId'] != 139393].index, inplace = True)
df.drop(df[df['eventName'] != "Pass"].index, inplace = True)
df.drop(df[df['matchPeriod'] != "1H"].index, inplace = True)
#exclude irrelevant columns
df['xstart']=0
df['ystart']=0
df['xend']=0
df['yend']=0
for i in df.index:
   df.at[i, "xstart"] = df.at[i,"positions"][0]['x']
   df.at[i, "ystart"] = df.at[i,"positions"][0]['y']
   df.at[i, "xend"] = df.at[i,"positions"][1]['x']
   df.at[i, "yend"] = df.at[i,"positions"][1]['y']
df = df[columns]



createPitch()

for i in df.index:
    plt.plot([int(df["xstart"][i]),int(df["xend"][i])],
             [int(df["ystart"][i]),int(df["yend"][i])], 
             color="blue")
    
    plt.plot(int(df["xstart"][i]),int(df["ystart"][i]),"o", color="green")
    
plt.show()

