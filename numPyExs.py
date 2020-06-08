# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 13:06:43 2020

@author: Alfredo
"""

import numpy as np

#Every 4 years since 1930
WCYears = np.arange(1930,2018,4)
#No World Cup in 1942 or 1946
WCYears = np.delete(WCYears,(3,4))


WCYears = [2002,2006,2010,2014]
WCHosts = ["Japan/Korea","Germany","South Africa","Brazil"]
WCWinners = ["Brazil","Italy","Spain","Germany"]
WCArray = np.array((WCYears,WCHosts,WCWinners))


WCYears = np.array([1966,1970,1974,1978])
WCTopScorers = np.array(["Eusebio","Muller","Lato","Kempes"])
WCGoals = np.array([9,10,7,6])

WCGoals>8

WCTopScorers[(WCGoals>8)]