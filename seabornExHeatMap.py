# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:08:14 2020

@author: Alfredo
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("players_20.csv")
cols = list(range(44)) + list(range(78,104))
data.drop(data.columns[cols],axis=1,inplace=True)


fig, ax = plt.subplots()
fig.set_size_inches(14, 10)
ax=sns.heatmap(data.corr())