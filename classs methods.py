# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 14:32:07 2025

@author: ROPAFADZOCHELSEAMUDA
"""
class Person:
    def __init__(self,name,age):
        """SELF REFERENCES THE CLASS ITS SELF  """
        self.name=name
        self.age=age
    def myfunc(self):
       print("Hello my name is"+ self.name)
       print("My age", self.age)
p1 = Person("John",36)
# del p1.age
p1.myfunc()            