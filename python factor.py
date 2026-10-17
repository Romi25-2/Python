# -*- coding: utf-8 -*-
"""
Created on Wed Jun  4 10:08:38 2025

@author: ROPAFADZOCHELSEAMUDA
"""
"""
n = int(input("Enter a number to compute the factorial:"))
def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(n))  """
def factor(n):
    prd = 1
    for x in range(1,n):
        prd *=x
        print( 'factorial is : ',str(n))
factor(5)