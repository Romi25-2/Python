# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 15:11:49 2025

@author: ROPAFADZOCHELSEAMUDA
"""

age = int(input("Enter your age:"))
purchase_amt = float(input("Enter your purchase amount:"))
fifteen_discount = purchase_amt * 0.15
ten_discount = purchase_amt * 0.10
if  12 <= age >= 65 :
    print("Final Price",fifteen_discount)
else:
         print ("No discount")
if 12 >= age <=65 and purchase_amt >=100: 
    print("Final Price",ten_discount)      
else :
        print("No Discount")