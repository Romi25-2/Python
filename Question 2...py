# -*- coding: utf-8 -*-
"""
Created on Thu May 29 11:40:54 2025

@author: ROPAFADZOCHELSEAMUDA
"""

import math

def ln_approximation(x, precision, max_terms):

    current_term = x  # First term in the series
    total_approx = current_term  # Running total
    previous_total = 0  # Previous total for differnce calculation
    terms_used = 1  # Count of terms used

    print(f"Term  {terms_used} : {current_term:.10f}, Running Total: {total_approx:.10f}, Difference: {abs(total_approx - previous_total):.10f}")

#looping until precision or max terms is reahed
    while terms_used < max_terms:
         previous_total = total_approx
         current_term *= -x / (terms_used + 1)  #Formular for the next term in the series 
         total_approx += current_term
         terms_used += 1 

         print(f"Term  {terms_used} : {current_term:.10f}, Running Total: {total_approx:.10f}, Difference: {abs(total_approx - previous_total):.10f}")
 
         if abs(total_approx - previous_total) < precision:
            break

    return total_approx, terms_used 


def main():
    while True:
        try:
            x = float(input("Enter a value for x (-1 < x < 1): "))
            if -1 < x < 1:
                break
            else:
                print("Error: Value within the range -1 < x < 1.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    try:      
        precision = float(input("Enter the desired precision (e.g., 0.000001): "))
        max_terms = int(input("Enter the maximum number of terms: "))
    except ValueError:
        print("Invalid input.Exiting.")
        return
    #Performs the approximation
    approximation, terms_used = ln_approximation(x, precision, max_terms)
    exact_value = math.log(1 + x) 
    difference = abs(approximation - exact_value)

    print("\nSummary:")
    print(f"Final approximation of ln(1 + {x}): {approximation:.10f}")
    print(f"Exact value of ln(1 + {x}): {exact_value:.10f}")
    print(f"Number of terms used: {terms_used}")
    print(f"Difference between approximation and exact value: {difference:.10f}")


if __name__ == "__main__":
    main()
