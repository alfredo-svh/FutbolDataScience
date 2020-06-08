# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:51:10 2020

@author: Alfredo
"""



import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import squarify

data = pd.read_csv("MCPlayers.csv")

dataGoals = data[data["G"]>1]
norm = matplotlib.colors.Normalize(vmin=min(dataGoals.G), vmax=max(dataGoals.G))
colors = [matplotlib.cm.Blues(norm(value)) for value in dataGoals.G]
fig = plt.gcf()
ax = fig.add_subplot()
fig.set_size_inches(16, 4.5)
squarify.plot(label=dataGoals.Player,sizes=dataGoals.G, color = colors, alpha=.6)
plt.title("Man City Goals",fontsize=23,fontweight="bold")
plt.axis('off')
plt.show()

dataAssists = data[data["A"]>0]
norm = matplotlib.colors.Normalize(vmin=min(dataAssists.A), vmax=max(dataAssists.A))
colors = [matplotlib.cm.Blues(norm(value)) for value in dataAssists.A]
fig = plt.gcf()
fig.set_size_inches(16, 4.5)
squarify.plot(label=dataAssists.Player,sizes=dataAssists.A, color = colors, alpha=.6)
plt.title("Man City Assists",fontsize=23,fontweight="bold")
plt.axis('off')
plt.show()