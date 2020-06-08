# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 17:55:43 2020

@author: Alfredo
"""


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("fantasy.csv")


sns.pairplot(data, vars=["now_cost","selected_by_percent","total_points"],  kind="reg")
plt.show()