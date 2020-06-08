# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:03:29 2020

@author: Alfredo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import seaborn as sns


def createPitch():
    
    #Create figure
    fig=plt.figure()
    fig.set_size_inches(7, 5)
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


data = pd.read_json("events_World_Cup.json")

player = 139393
match = 2057954
data = data[data['playerId']==player]
data = data[data['matchId']==match]
data = data[data['eventName']=="Pass"]
data['xstart']=0
data['ystart']=0
data['xend']=0
data['yend']=0
for i in data.index:
   data.at[i, "xstart"] = data.at[i,"positions"][0]['x']
   data.at[i, "ystart"] = data.at[i,"positions"][0]['y']
   data.at[i, "xend"] = data.at[i,"positions"][1]['x']
   data.at[i, "yend"] = data.at[i,"positions"][1]['y']
   

fig, ax = plt.subplots()
fig.set_size_inches(14, 4)
#Plot one - include shade
plt.subplot(121)
sns.kdeplot(data["xstart"],data["ystart"], shade="True")
#Plot two - no shade, lines only
plt.subplot(122)
sns.kdeplot(data["xstart"],data["ystart"])


fig, ax = plt.subplots()
fig.set_size_inches(14, 4)
#Plot One - distinct areas with few lines
plt.subplot(121)
sns.kdeplot(data["xstart"],data["ystart"], shade="True", n_levels=5)
#Plot Two - fade lines with more of them
plt.subplot(122)
sns.kdeplot(data["xstart"],data["ystart"], shade="True", n_levels=40)


createPitch()
sns.kdeplot(data["xstart"],data["ystart"], shade="True", n_levels=50)
plt.ylim(0, 90)
plt.xlim(0, 130)
plt.show()