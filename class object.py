# -*- coding: utf-8 -*-
"""
object and classes 
encapsulation
methos and ariables - methods are functins 
inheritence
message 
attributs are the same thing 
Object or classs conrains data and the function that operate on that data 
1 class =  multiple objects
class is a blueprint of and object 
objects are like houses build on the blue print 
attributes - memebrs of a class and are characteristics
functions - behaviours of an object 
init= initiate

OOP importants ; data hiding amd public interface 
CONSTRUCUTER IS A PUBLIC FUNCTION 
"""

'''creating a class '''
class Account: '''add a capital letter at the start'''
acctNum=''
balance =0

def _init_(self,account_number,balance):
    self .acctNum = acctNum
    self.balance=balance
    
def deposit(self,balance):
    balance += float(input('ENTER AMOUNT TO BE DEPOSITED'))
    print('Deposit successful \n Your balance is:',balance)

def withdrawl(self,balance):
    balance-=float(input=('ENTER WIDTHRAWL AMOUNT '))
    
john=Account(987654,300)    
print('Account Number',john.acctNum)
print('Balance>>',john.balance)