# -*- coding: utf-8 -*-
"""
Created on Tue Apr 22 11:35:24 2025

@author: ROPAFADZOCHELSEAMUDA
"""

#default account
balance=1000

while True :
    print("\n==ATM MENU===")
    print("1-Check Balance")
    print("2-Withdraw money")
    print("3-Deposit Money")
    print("4-Fast cash")
    choice = int(input("Please choose transactions:")) 
    if choice== '1':
        print(f"Your current balance is:$(balance")
        
    elif choice== '2':
            try:
                amount = float(input("Enter amount to withdraw:"))
                if amount <=0:
                    print("Please enter a positive amount.")
                elif amount > balance:
                    print("Insufficient funds.")
                else:
                        balance -= amount
                        print(f"Withdraw succesful.New balance:$(balance")
            except ValueError:
                        print("Invalid amount. Please eneter  number")
   elif choice =='3'
                   try:
                        
             