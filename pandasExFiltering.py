# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 16:04:00 2020

@author: Alfredo
"""

import numpy as np
import pandas as pd 

def filterByClub(team):
    return data[data['club'] == team][['short_name','wage_eur','value_eur','player_positions','overall','age']]

def cheaperReplacement(player, skillReduction=0):
    playerWage = player['wage_eur'].item()
    playerPos = player['player_positions'].item()
    playerRating = player['overall'].item() - skillReduction
    playerAge = player['age'].item()
    
    longlist = data[data['player_positions'] == playerPos][['short_name','wage_eur','value_eur','player_positions','overall','age']]
    longlist.drop(longlist[longlist['overall'] < playerRating].index , inplace=True)
    longlist.drop(longlist[longlist['wage_eur'] >= playerWage].index, inplace=True)
    longlist.drop(longlist[longlist['age'] > playerAge].index, inplace=True)
    return longlist.sort_values("wage_eur")
    
    

data = pd.read_csv("players_20.csv")    

manUtdPlayers = filterByClub("Manchester United").sort_values("wage_eur", ascending = False)

DDG = manUtdPlayers[manUtdPlayers['short_name'] == 'De Gea'][['short_name','wage_eur','value_eur','player_positions','overall','age']]
Fred = manUtdPlayers[manUtdPlayers['short_name'] == 'Fred'][['short_name','wage_eur','value_eur','player_positions','overall','age']]
Lindelof = manUtdPlayers[manUtdPlayers['short_name'] == 'V. Lindelöf'][['short_name','wage_eur','value_eur','player_positions','overall','age']]
Pogba = manUtdPlayers[manUtdPlayers['short_name'] == 'P. Pogba'][['short_name','wage_eur','value_eur','player_positions','overall','age']]

replacements = cheaperReplacement(Pogba, 8)