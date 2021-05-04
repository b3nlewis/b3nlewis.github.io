# -*- coding: utf-8 -*-
"""
agentframework file which includes moving, eating and sharing.

@author: b3nle
"""
#import packages
import random
     
# Agent Class   
class Agent():
     def __init__(self, environment, agents, neighbourhood):
        self._x = random.randint(0,300)
        self._y = random.randint(0,300)
        self.environment = environment
        self.agents = agents
        self.store = 0
        
     def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
     def eat(self): # Dictates how much is eaten, less than zero nothing, less than 10 all remaining and more than 10 is 10.
         if self.store > 100: # agents sick up food.
             self.store -= 100
             self.environment[self.y][self.x] += 100
         elif self.environment[self.y][self.x] <= 0:
             return
         elif self.environment[self.y][self.x] > 10:
             self.environment[self.y][self.x] -= 10
             self.store += 10
         else:#less than 10, eat remaining
             remaining = self.environment[self.y][self.x]
             self.environment[self.y][self.x] -= remaining
             self.store += remaining
             
     def share_with_neighbours(self, neighbourhood):
         for agents in self.agents:
             distance = self.distance_between(agents)
             if distance <= neighbourhood:
                 ave = (self.store + agents.store)/2
                 self.store = ave
                 agents.store = ave
                 #print("sharing " + str(distance) + " " + str(ave))
         
     def distance_between(self, agents): 
            return (((self.x - agents.x)**2) +
            ((self.y - agents.y)**2))**0.5   

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