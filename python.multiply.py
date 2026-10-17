# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 10:39:51 2025

@author: ROPAFADZOCHELSEAMUDA
"""
num= int(input("Enter a number"))
def multiply(num):
    prod = 1
    for num in num:
        prod *= num
    return prod
multi_list = [1,14,15]
print(multiply(multi_list))