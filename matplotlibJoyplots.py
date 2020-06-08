# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 01:40:02 2020

@author: Alfredo
"""

from __future__ import unicode_literals
import joypy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

df = pd.read_csv("top50-00-19.csv")

fig, axes = joypy.joyplot(df[df.Player != 'Neymar'],by="Season", column="Value", ylabels=False, xlabels=False, 
                          grid=False, fill=False, background='k', linecolor="w", linewidth=1, x_range=[-60,110],
                          legend=False, overlap=0.5, figsize=(6,5),kind="counts", bins=80)

plt.text(0, 0.96, "Top 50 transfer values (€m) In 2000-2019",fontsize=12,color="white")
plt.show()