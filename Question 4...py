# -*- coding: utf-8 -*-
"""
Created on Thu May 29 14:32:06 2025

@author: ROPAFADZOCHELSEAMUDA
"""

def update_account():
    # Get customer account details
    acct_num = input("Enter account number: ")
    acct_type = input("Enter account type ('s' for savings, 'c' for checking): ").lower()
    min_balance = float(input("Enter minimum account balance: "))
    current_balance = float(input("Enter current account balance: "))

    service_charge = 0
    interest = 0
    message = ""

    # Check account type and calculate charges or interest
    if acct_type == 's':
        if current_balance < min_balance:
            service_charge = 10.00 # charge for savings accounts
            message = "Service charge applied: $10.00"
        else:
            interest = current_balance * 0.04 #4% interest
            message = f"Interest applied: ${interest:.2f}"
   
    elif acct_type == 'c':
        if current_balance < min_balance:
            service_charge = 25.00 #checking accounts
            message = "Service charge applied: $25.00"
        else:
            if current_balance <= min_balance + 5000:
                interest = current_balance * 0.03 #3% interest 
            else:
                interest = current_balance * 0.05 #5% interest
            message = f"Interest applied: ${interest:.2f}"
    else:
        message = "Invalid account type entered."
        print(message)
        return
    
    # Update balance
    current_balance = current_balance - service_charge + interest

    # Output account details and message
    print(f"Account Number: {acct_num}")
    print(f"Account Type: {'Savings' if acct_type == 's' else 'Checking'}")
    print(f"Current Balance: ${current_balance:.2f}")
   
update_account()
