# -*- coding: utf-8 -*-
"""
A basic Agent Based Model, which creates two agents 
in random locations within a 100x100 grid and moves
them randomly three times.

The code has been shrunk compared to the second practical
by creating implementing for loops to shrink the code.

@author: b3nle
"""

#Modules to import.
import random
import operator
import matplotlib.pyplot as plt

#Variables
num_of_agents = 10 #set number of agents in model.
num_of_iterations = 10 #set number of iterations for model.
agents = []#empty list for agents.

# Create list of agents with a set of random coordinates.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#moves agents each iterations.
for i in range(num_of_iterations):
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i][0] += 1 % 100
        else:
            agents[i][0] -= 1 % 100
            
        if random.random() < 0.5:
            agents[i][1] += 1 % 100
        else:
            agents[i][1] -= 1 % 100


#Work out furthest East agent.
east=(max(agents, key=operator.itemgetter(1)))

#Create graph to show agent locations.
plt.ylim(0, 99)
plt.xlim(0, 99)
for i in range(num_of_agents):
    plt.scatter(agents[i][1],agents[i][0])
plt.scatter(east[1], east[0], color='red')
plt.show()
    
#Work out euclidean distance between two sets of y and xs.
#answer = (((y0 - y1)**2) + ((x0 -x1)**2))**0.5
#print(answer)