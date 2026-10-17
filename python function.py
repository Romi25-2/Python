# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 09:04:37 2025

@author: ROPAFADZOCHELSEAMUDA
"""
#write a python function to check whetehr a number falls within a given range

def test_range(n) :
    if n in range(1,15):
        print("%s is in the range" % str(n))
    else :
        print("Number is outisde the given range")
test_range(5) 

"""
def test_range(num,start,last) :
    if start,num,last:
        print("%s is in the range" % str(num))
    else :
        print("Number is not in range")
test_range(21,53,200)  
"""