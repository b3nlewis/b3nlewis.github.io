# -*- coding: utf-8 -*-
"""
A basic Agent Based Model, which creates two agents 
in random locations within a 100x100 grid and moves
them randomly three times.

The code has been shrunk compared to the first practical
by creating an agents list, and appending agents values
into that list.

@author: b3nle
"""

#Modules to import.
import random
import operator
import matplotlib.pyplot as plt

#Variables
agents = []#empty list for agents.

# Create first set of variables and append to list.
agents.append([random.randint(0,99),random.randint(0,99)])

#Change y and x randomly, first time.
if random.random() < 0.5:
    agents[0][0] += 1
else: 
    agents[0][0] -= 1
if random.random() < 0.5:
    agents[0][1] += 1
else: 
    agents[0][1] -= 1
    
#Change y and x randomly, second time.
if random.random() < 0.5:
    agents[0][0] += 1
else: 
    agents[0][0] -= 1
if random.random() < 0.5:
    agents[0][1] += 1
else: 
    agents[0][1] -= 1
    
#Change y and x randomly, third time.
if random.random() < 0.5:
    agents[0][0] += 1
else: 
    agents[0][0] -= 1
if random.random() < 0.5:
    agents[0][1] += 1
else: 
    agents[0][1] -= 1


# Create second set of variables.
agents.append([random.randint(0,99),random.randint(0,99)])

#Change y and x randomly, first time.
if random.random() < 0.5:
    agents[1][0] += 1
else: 
    agents[1][0] -= 1
if random.random() < 0.5:
    agents[1][1] += 1
else: 
    agents[1][1] -= 1
    
#Change y and x randomly, second time.
if random.random() < 0.5:
    agents[1][0] += 1
else: 
    agents[1][0] -= 1
if random.random() < 0.5:
    agents[1][1] += 1
else: 
    agents[1][1] -= 1
    
#Change y and x randomly, third time.
if random.random() < 0.5:
    agents[1][0] += 1
else: 
    agents[1][0] -= 1
if random.random() < 0.5:
    agents[1][1] += 1
else: 
    agents[1][1] -= 1

#Work out furthest East agent.
east=(max(agents, key=operator.itemgetter(1)))

#Create graph to show agent locations.
plt.ylim(0, 99)
plt.xlim(0, 99)
plt.scatter(agents[0][1],agents[0][0])
plt.scatter(agents[1][1],agents[1][0])
plt.scatter(east[1], east[0], color='red')#shows furthest east agent.
plt.show()
    
#Work out euclidean distance between two sets of y and xs.
#answer = (((y0 - y1)**2) + ((x0 -x1)**2))**0.5
#print(answer)