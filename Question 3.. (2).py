# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:12:56 2025

@author: ROPAFADZOCHELSEAMUDA
"""

def print_house():
    # the roof  pattern
    for i in range(5):  # Height of the roof
    
        for j in range(4 - i):  # Spaces before the roof
            print("  ", end="  ")
            
        for k in range(2 * i + 1):  
            print("* ", end="  ")        
        print()  

   #the base pattern
    for i in range(1, 5):  # Height of the base, starting from the second row
        for j in range(1):  # Spaces before the base to center it
            print("  ", end="  ")
        for j in range(7):  # Width of the base
            if i == 4 or j == 0 or j == 6:
                print("* ", end="  ")  
            else:
                print("  ", end="  ")  
        print()  

print_house()
