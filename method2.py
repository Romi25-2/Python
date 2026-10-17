# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:06:55 2025

@author: ROPAFADZOCHELSEAMUDA
"""

class Person:
    def __init__(self,name,age):
        """SELF REFERENCES THE CLASS ITS SELF  """
        self.name=name
        self.age=age
        """creating methods"""   
    def myfunc(self):
            print("Hello my name is"+ self.name)
p1=Person("John",36)
p2=Person("Romi",20)
"""'modify parameters"""
p1.age=40     
print(p1.name)
print(p1.age)
print(p2.name)
print(p2.age)

p1.myfunc()
