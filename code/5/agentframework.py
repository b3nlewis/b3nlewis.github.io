# -*- coding: utf-8 -*-
"""
agentframework file which creates agents in a random location and then moves
agents everytime the move function is defined. X and Y variables are protected
using get and set functions.

@author: b3nle
"""
#import packages
import random
     
# Agent Class   
class Agent():
     def __init__(self):
        self._x = random.randint(0,99)
        self._y = random.randint(0,99)
        
     def move (self):
         if random.random() < 0.5:
            self._y += 1 % 100
         else:
            self._y -= 1 % 100
            
         if random.random() < 0.5:
            self._x += 1 % 100
         else:
            self._x -= 1 % 100
            
     def setx(self, value):
        self._x = value
        
     def sety(self, value):
        self._y = value 
           
     def getx(self):
        return self._x
    
     def gety(self):
        return self._y

     x = property(getx, setx)
     y = property(gety, sety)