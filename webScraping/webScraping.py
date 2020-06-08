# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 15:25:37 2020

@author: Alfredo
"""

from lxml import html
import requests
from bs4 import BeautifulSoup
from os.path  import basename
import pandas as pd
import numpy as np
import re

headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}


    
#Top 25 transfers of each season from 2000/01 - 2019/20
season =2000
playersList = []
valuesList = []
seasonList = []

while season<=2019:
    page = "https://www.transfermarkt.co.uk/transfers/transferrekorde/statistik/top/plus/0/galerie/0?saison_id=" + str(season)
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    players = pageSoup.find_all("a", {"class": "spielprofil_tooltip"})
    values = pageSoup.find_all("td", {"class": "rechts hauptlink"})
    
    for i in range(25):
        playersList.append(players[i].text)
        valuesList.append(values[i].text)
        seasonList.append(season)
    season+=1   
df = pd.DataFrame({"Players":playersList,"Values":valuesList, "Season":seasonList})



#-------------------------------------------------------------------------



#Save player images of entire league
page = 'https://www.transfermarkt.co.uk/liga-mx-clausura/startseite/wettbewerb/MEX1'
tree = requests.get(page, headers = headers)
soup = BeautifulSoup(tree.content, 'html.parser')

teamLinks = []
playerLinks = []
links = soup.select("a.vereinprofil_tooltip")

#find the link for each team in the league
for i in range(0,54,3):
    teamLinks.append("https://www.transfermarkt.co.uk" + links[i].get("href"))
    
#find the link for each player on every team in the league
for i in range(len(teamLinks)):
    page = teamLinks[i]
    tree = requests.get(page, headers = headers)
    soup = BeautifulSoup(tree.content, 'html.parser')

    links = soup.select("a.spielprofil_tooltip")
    
    for j in range(len(links)):
        playerLinks.append("https://www.transfermarkt.co.uk" + links[j].get("href"))

#removing duplicates
playerLinks = list(set(playerLinks))

#find and save the profile picture of every player in the league
for i in range(len(playerLinks)):
    page = playerLinks[i]
    tree = requests.get(page, headers=headers)
    soup = BeautifulSoup(tree.content, 'html.parser')
    
    name = soup.find_all("h1")
    image = soup.find_all("img",{"title":name[0].text})
    src = image[0].get('src').split("?lm")[0]

    #Save the image under the player's name
    with open(name[0].text + ".jpg","wb") as f:
        f.write(requests.get(src).content)



#--------------------------------------------------------------------------
        
        

#Save player data
page = requests.get('https://ligamx.net/cancha/tablas/tablaGeneralClasificacion/sp/8934b8c89a62e0')
tree = html.fromstring(page.content)

linkLocation = tree.cssselect('.col-xs-3')
teamLinks = []
playerLinks = []

name = []
team = []
age = []
apps = []
height = []
weight = []

for i in range(18):
    teamLinks.append('https://ligamx.net/' + linkLocation[i].attrib['href'])

for i in range(len(teamLinks)):
    squadPage = requests.get(teamLinks[i])
    squadTree = html.fromstring(squadPage.content)
    
    tm = squadTree.cssselect('#tituloMail')[0].text
    playerLocation = squadTree.cssselect('div.jugador a')

    for i in range(len(playerLocation)):
        tmp = playerLocation[i].attrib['href']
        if tmp.find("cuerpotecnico") == -1:
            playerLinks.append('https://ligamx.net' + tmp)
            team.append(tm)
            
for i in range(len(playerLinks)):
    playerPage = requests.get(playerLinks[i])
    playerTree = html.fromstring(playerPage.content)

    tempName = str(playerTree.cssselect('h1.nombre')[0].text_content())
    
    try:  
        tempAge = int(playerTree.cssselect('dd')[3].text_content()[0:2])
    except IndexError:
        tempAge = float('NaN')

    try:
        tempApps = int(playerTree.cssselect('span.numero')[0].text_content())
    except IndexError:
        tempApps = float('NaN')

    try:
        tempHeight = float(playerTree.cssselect('dd')[4].text_content())
    except IndexError:
        tempHeight = float('NaN')

    try:
        tempWeight = float(playerTree.cssselect('dd')[5].text_content().split(' ')[0])
    except IndexError:
        tempWeight = float('NaN')

    name.append(tempName)
    age.append(tempAge)
    apps.append(tempApps)
    height.append(tempHeight)
    weight.append(tempWeight)

df = pd.DataFrame(
    {'Name':name,
     'Team':team,
     'Age':age,
     'Apps':apps,
     'HeightCM':height,
     'WeightKG':weight})
df.to_csv("LigaMXData.csv")