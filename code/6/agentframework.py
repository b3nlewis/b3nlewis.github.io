# -*- coding: utf-8 -*-
"""
agentframework file which includes moving,

@author: b3nle
"""
#import packages
import random
     
# Agent Class   
class Agent():
     def __init__(self, environment):
        self._x = random.randint(0,249)
        self._y = random.randint(0,249)
        self.environment = environment
        self.store = 0
        
     def move (self):
         if random.random() < 0.5:
            self._y += 1 % 100
         else:
            self._y -= 1 % 100
            
         if random.random() < 0.5:
            self._x += 1 % 100
         else:
            self._x -= 1 % 100
            
     def eat (self): # Dictates how much is eaten, less than zero nothing, less than 10 all remaining and more than 10 is 10.
         if self.store > 100: # agents sick up food.
             self.store -= 100
             self.environment[self._y][self._x] += 100
         elif self.environment[self._y][self._x] <= 0:
             return
         elif self.environment[self._y][self._x] > 10:
             self.environment[self._y][self._x] -= 10
             self.store += 10
         else:#less than 10, eat remaining
             remaining = self.environment[self._y][self._x]
             self.environment[self._y][self._x] -= remaining
             self.store += remaining

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