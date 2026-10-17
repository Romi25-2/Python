d# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 09:30:53 2025

@author: ROPAFADZOCHELSEAMUDA
"""

class Account:
    """Add a capital letter at the start"""

    def __init__(self, account_number, balance):
        self.acctNum = account_number
        self.balance = balance

    def deposit(self):
        amount = float(input('ENTER AMOUNT TO BE DEPOSITED: '))
        self.balance += amount
        print('Deposit successful\nYour balance is:', self.balance)

    def withdrawal(self):
        amount = float(input('ENTER WITHDRAWAL AMOUNT: '))
        if amount > self.balance:
            print('Insufficient funds.')
        else:
            self.balance -= amount
            print('Withdrawal successful\nYour balance is:', self.balance)

# Create an account instance
john = Account(987654, 300)

# Display account details
print('Account Number>>', john.acctNum)
print('Balance >>', john.balance)
