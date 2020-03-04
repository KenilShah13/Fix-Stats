#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 16:55:04 2020

Step 1 – Write a python 3.7 script capable of generating fake FIX messages, 
the candidate needs to use the below description and online 
FIX 4.2 documentation. The script should be able to take 1 argument to 
specify the amount of fake FIX messages to generate.

expected format - (8=FIX.4.2|35=D|55=SYMBOL_1|54=1|38=100|40=2|59=0|167=FUT|1=CLIENT_1|44=199.99)

@author: kenilshah
"""

#for 
import sys
import random

def createFix():
    
    #print(num_of_records)
    
    fixed_values = {'54': ['1','2'],
                    '40': ['1','2','3','4','5'],
                    '59': ['0','1','2','3','4','5','6'],
                    '167': ['FUT','OPT','CS']}
    
    
    fixFile = open('fakeFix.txt', 'w')
    
    for _ in range(num_of_records):
        
        #55(Symbol meaning the product name: N is a number)
        product_name = random.randint(1,1000)
        
        #54(buy or sell the given symbol/product)
        buy_or_sell = random.choice(fixed_values['54'])
        
        #38(quantity of the symbol/product that you want to buy or sell)
        quantity_of_product = random.randint(1,100000)
        
        #40(only order types 1-5)
        order_type = random.choice(fixed_values['40'])
        
        #59(all time in force orders)
        time_force_order = random.choice(fixed_values['59'])
        
        #167(Futures, Options, Common stocks, etc)
        contract_type = random.choice(fixed_values['167'])
        
        #1(random client id)
        client_id = random.randint(1,1000)
        
        #44(Float field representing a price. Note the number of decimal places may vary)
        price = random.uniform(0,100000)
        
        
        record = f"8=FIX.4.2|35=D|55=SYMBOL_{product_name}|54={buy_or_sell}|" +\
                f"38={quantity_of_product}|40={order_type}|59={time_force_order}|" +\
                f"167={contract_type}|1=CLIENT_{client_id}|44={price}\n"
        
        fixFile.write(record)
        
        
        
        #print(record)
    print("fakeFix.txt created!")
    fixFile.close()


if __name__ == '__main__':
    
    if len(sys.argv) != 2: 
        
        print ("Please use format: 'python generateFakeFix.py num_of_records_to_generate'")
        exit(1)
    
    num_of_records = int(sys.argv[1])
    
    createFix()

