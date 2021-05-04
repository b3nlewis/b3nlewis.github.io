# -*- coding: utf-8 -*-
"""
A basic Agent Based Model, which creates two agents 
in random locations within a 100x100 grid and moves
them randomly three times.

A function has been added to this model, to calculate the distance between
agents.

@author: b3nle
"""

#Modules to import.
import random
import operator
import matplotlib.pyplot as plt
import time

start = time.process_time()

#Functions
def distance_between(agents_row_a, agents_row_b):
    ''' A function to calculate the distance between agent a and agent b.
    Args:
        a: A list of two coordinates for orthoganol axes.
        b: A list of two coordinates for the same orthoganol axes as a.
    Returns:
        The straight line distance between the a and b in the an plane given
        by two orthoganol axes. '''
    return (((agents_row_a[0] - agents_row_b[0])**2)+((agents_row_a[1] - agents_row_b[1])**2)*0.5)

#Variables
num_of_agents = 10 #set number of agents in model.
num_of_iterations = 100
agents = []#empty list for agents.

# Create list of agents with a set of random coordinates.
for i in range(num_of_agents):
    agents.append([random.randint(0,99),random.randint(0,99)])

#moves agents each iteration.
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
plt.ylim(0, 100)
plt.xlim(0, 100)
for i in range(num_of_agents):
    plt.scatter(agents[i][1],agents[i][0])
plt.scatter(east[1], east[0], color='red')
plt.show()
    
#Work out euclidean distance between two sets of y and xs.
maxdistance = distance_between(agents[0], agents[1])
mindistance = maxdistance
for i in range(num_of_agents):
    for j in range(i, num_of_agents):# so does not repeat pairs.
         if i != j:#so agents do not test against themselves.
            distance = distance_between(agents[i], agents[j])
            maxDistance = max(maxdistance, distance)
            minDistance = min(mindistance, distance)
        
#Find max and min of distances
print("Min Distance: ", minDistance)
print("Max Distance: ", maxDistance)

end = time.process_time()
print("Time: ",end-start)
