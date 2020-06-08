# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:54:09 2020

@author: Alfredo
"""

import random


def calculateWinner(homexG, awayxG):
    homeGoals = 0
    awayGoals = 0
    
    for xG in homexG:
        if random.random() <= xG:
            homeGoals +=1
    
    for xG in awayxG:
        if random.random() <= xG:
            awayGoals +=1
    
    if homeGoals > awayGoals:
        return "home"
        #print("Home wins! " + str(homeGoals) + " - " + str(awayGoals))
    elif awayGoals > homeGoals:
        return "away"
        #print("Away wins! " + str(homeGoals) + " - " + str(awayGoals))
    else:
        return "draw"
        #print("Share of the points! " + str(homeGoals) + " - " + str(awayGoals))


HomexG = [0.21,0.66,0.1,0.14,0.01]
AwayxG = [0.04,0.06,0.01,0.04,0.06,0.12,0.01,0.06]

TotHomexG = sum(HomexG)
TotAwayxG = sum(AwayxG)
home=0
away = 0
draw = 0

for i in range(10000):
    res = calculateWinner(HomexG, AwayxG)
    if res=="home":
        home+=1
    elif res == "away":
        away+=1
    else:
        draw+=1

print("Over 10000 games, home wins " + str(home/100) + "%, away wins " + str(away/100) + "% and there is a draw in " + str(draw/100) + "% of games.")