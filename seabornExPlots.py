# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 22:55:09 2020

@author: Alfredo
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("players_20.csv")
df['attacking_work_rate'] = ""
df['defending_work_rate'] = ""
CSL = ["Guangzhou Evergrande Taobao FC","Beijing Sinobo Guoan FC","Shanghai SIPG FC","Jiangsu Suning FC","Guangzhou R&F FC","Hebei China Fortune FC","Shanghai Greenland Shenhua FC","Shandong Luneng TaiShan FC","Dalian YiFang FC","Tianjin Quanjian FC","Tianjin TEDA FC","Chongqing Dangdai Lifan FC SWM Team","Henan Jianye FC","Beijing Renhe FC","Wuhan Zall","Shenzhen FC"]
CSLcols = ("#FF0000", "#9A050A", "#112987", "#00A4FA", "#FF6600", "#008040", "#004EA1", "#5B0CB3", "#E50211", "#FF0000", 
           "#00519A",  "#75A315", "#E70008", "#E40000", "#C80815", "#FF3300")
#note: this colors don't accuratelly represent their respective team

for i in df.index:
    wr = df.at[i,"work_rate"].split("/")
    df.at[i, "attacking_work_rate"] = wr[0]
    df.at[i, "defending_work_rate"] = wr[1]


#scatter plots
sns.regplot(x="height_cm",y="weight_kg",data=df)
sns.regplot(x="attacking_finishing",y="goalkeeping_handling",data=df,
           color="green")
sns.regplot(x="skill_long_passing",y="attacking_short_passing",data=df,
           scatter_kws={'alpha':0.07})
sns.lmplot(x="attacking_crossing",y="attacking_finishing",data=df,
           scatter_kws={'alpha':0.1},
           col="preferred_foot",
           row="attacking_work_rate",
           aspect=2, size=2
           )



df = df[df['club'].isin(CSL)]
CSLpalette = sns.color_palette(CSLcols)

#box plots
fig, ax = plt.subplots()
fig.set_size_inches(14, 5)
ax = sns.boxplot(x="club", y="age", data=df, palette = CSLpalette)
plt.xticks(rotation=65)


#Violin Plots
fig, ax = plt.subplots()
fig.set_size_inches(14, 5)
ax = sns.violinplot(x="club", y="age", data=df, palette = CSLpalette)
plt.xticks(rotation=65)
plt.show()