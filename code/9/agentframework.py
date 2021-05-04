# -*- coding: utf-8 -*-
"""
agentframework file which includes moving, eating environment and sharing resources.

@author: b3nle
"""
#import packages
import random
     
# Agent Class   
class Agent():
     def __init__(self, environment, agents, neighbourhood, y=None, x=None):#defaults are set to None.
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x*3 #times 3 to fill enitre map, html only went to 100.
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y*3
        self.environment = environment
        self.agents = agents
        self.store = 0
        
     def move (self):
        if random.random() < 0.5:
            self._y = (self._y + 1) % 300#Modulus taken so that environment is finite, agents will go to opposite side.
        else:
            self._y = (self._y - 1) % 300

        if random.random() < 0.5:
            self._x = (self._x + 1) % 300
        else:
            self._x = (self._x - 1) % 300
            
     def eat(self): # Dictates how much is eaten, less than zero nothing, less than 10 all remaining and more than 10 is 10.
         if self.store >= 60: # agents sick up food based upon random probability.
             if random.randint(0, 100) > 40:#Random probability of agents being sick
                 self.environment[self._y][self._x] += self.store
                 self.store = 0
         elif self.environment[self._y][self._x] > 10:#Greater than 10 food in environment.
             self.environment[self._y][self._x] -= 5
             self.store += 5
         elif self.environment[self._y][self._x] <= 0:
             return
         else:#less than 10, eat remaining
             remaining = self.environment[self._y][self._x]
             self.environment[self._y][self._x] -= remaining
             self.store += remaining
             
     def share_with_neighbours(self, neighbourhood):
         for agents in self.agents:
             distance = self.distance_between(agents)
             if distance <= neighbourhood:
                 if self.agents != agents:
                     ave = (self.store + agents.store)/2
                     self.store = ave
                     agents.store = ave
                     #print("sharing " + str(distance) + " " + str(self._x) + " " + str(agents._x) + " "+ str(ave))
         
     def distance_between(self, agents): 
            return (((self._x - agents._x)**2) +
                    ((self._y - agents._y)**2))**0.5   

#This keeps the x and y values safe from being changed unknowingly.
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