#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 19:33:43 2020

Step 2 – Write a python 3.7 script capable of reading the generated FIX messages and produce various statistics on the trading habits of each clients.

The type of stats could be the message amount per clients, list of all the traded products(symbols), most popular order type(40), average ordered quantity per product and most popular order rule (59). Please feel free to be creative and generate other stats. Produce at least 5 stats.

Please format to human readable for some fix tags (ex. 59) when you are doing the stat.

@author: kenilshah
"""

import numpy as nup
import collections as c
    
#Stat 1 - messages per clients
def getMessageAmountPerClient():
    
    clientColumn= [x.split('|')[8] for x in open(fakeFixFile).readlines()]
    value= [x.split('=')[1] for x in clientColumn]
    
    print("\nStat# 1: Top 3 client with most amount of message: \n")
    for key, count in c.Counter(value).most_common(3):
        print ('{}: {}'.format(key,count))
    
    

#Stat 2 - message amount per contract type
def getAmountPerContractType():
    
    contractColumn= [x.split('|')[7] for x in open(fakeFixFile).readlines()]
    value= [x.split('=')[1] for x in contractColumn]
    
    print("\nStat# 2: Message amount per contract type: \n")
    for key, count in c.Counter(value).most_common():
        print ('{}: {}'.format(key,count))
 
#Stat 3 - top 3 most quantity ordered for products per message
def getHighestQuantityOrdered():
    
    tempDict = {}
    
    for x in open(fakeFixFile).readlines():
        tempDict[(x.split('|')[2]).split('=')[1]] = (x.split('|')[4]).split('=')[1]
        
    #print(tempDict)
    
    k = c.Counter(tempDict) 
    
    high = k.most_common(3)

    
    print("\nStat# 3: Top 3 highest quantity ordered: \n")
    print("Symbol : Quantity ordered")
 
    for a in high:
        print(a[0]," :",a[1]," ") 
        
        
#Stat 4 - min/max/median price for buy and sell options where 1=buy 2=sell
def getStatsBuyAndSell():
    
    tempListBuy=[]
    tempListSell = []
    
    print("\nStat# 4: Pricing stats based on Buy or Sell: \n")
    
    for x in open(fakeFixFile).readlines():
        
        if ((x.split('|')[3]).split('=')[1]) == '1' :
            x = x.strip()
            tempListBuy.append(float((x.split('|')[9]).split('=')[1]))
    
    print('Buy Option - \n')
    print('Max price :', nup.max(tempListBuy))
    print('Min price :', nup.min(tempListBuy))
    print('Median price :', nup.median(tempListBuy))
        
    for x in open(fakeFixFile).readlines():
        
        if ((x.split('|')[3]).split('=')[1]) == '2' :
            x = x.strip()
            tempListSell.append(float((x.split('|')[9]).split('=')[1]))
            
    print('\n\nSell Option - \n')
    print('Max price :', nup.max(tempListSell))
    print('Min price :', nup.min(tempListSell))
    print('Median price :', nup.median(tempListSell))

#Stat 5 - number of messages per duration of order
def getMessageAmountPerDuration():
    
    temp1 = []
    for x in open(fakeFixFile).readlines():
        temp1.append((x.split('|')[6]).split('=')[1])
    
    print("\nStat# 5: number of messages per duration of order: \n")
       
    for key, count in sorted(c.Counter(temp1).most_common()):
        
        if(key == '0'):
            key = 'Day(0)'
        elif (key == '1'):
            key = 'Good Till Cancel(1)'
        elif (key == '2'):
            key = 'At the Opening(2)'
        elif (key == '3'):
            key = 'Immediate or Cancel(3)'
        elif (key == '4'):
            key = 'Fill or Kill(4))'
        elif (key == '5'):
            key = 'Good Till Crossing(5)'
        elif (key == '6'):
            key = 'Good Till Date(6)'
            
        print ('{}: {}'.format(key,count))


#Stat 6 - Products ordered multiple times(most popular)
def getMostPopularProduct():
        
    print("\nStat# 6: Top 5 products ordered multiple times: \n")
    
    symbolColumn= [x.split('|')[2] for x in open(fakeFixFile).readlines()]
    value= [x.split('=')[1] for x in symbolColumn]
    
    for key, count in c.Counter(value).most_common(5):
        print ('{}: {}'.format(key,count))




if __name__ == '__main__':
    
    fakeFixFile = 'fakeFix.txt'

    getMessageAmountPerClient()
    
    getAmountPerContractType()
    
    getHighestQuantityOrdered()
    
    getStatsBuyAndSell()
    
    getMessageAmountPerDuration()

    getMostPopularProduct()