# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:05:18 2021
This model has a cleaned look compared to previous versions with better
commenting and style. Timing is included to help debugging.
Agent locations and moving are controlled in agentframework rather than in
this script.

@author: b3nle
"""

import matplotlib.pyplot as plt
import agentframework
import time

def distance_between(agents_row_a, agents_row_b):
    '''
    

    Parameters
    ----------
    agents_row_a : A list of two coordinates
    agents_row_b : A list of two coordinates for another agent.

    Returns
    -------
    Euclidean distance between agent a and agent b

    '''
    return (((agents_row_a.x - agents_row_b.x)**2) +
        ((agents_row_a.y - agents_row_b.y)**2))**0.5

'''
Step 1: Initialise Parameters
'''
start = time.process_time()
print("Step 1: Initialise Parameters")
num_of_agents = 100
num_of_iterations = 100
agents = []#contains agents

'''
Step 2: Initialise agents.
'''
print("Step 2: Initialise agents")
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent())

'''
Step 3: Move agents using move method from agentframework.
'''
print("Step 3: Move agents using move method from agentframework")
# Move the agents every iteration.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        
'''
Step 4: Create a graph showing results.
'''
print("Step 4: Create a graph showing results")
plt.xlim(0, 100)
plt.ylim(0, 100)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

'''
Step 5: Calculate maximum and minimum distance between agents.
'''
print("Step 5: Calculate maximum and minimum distance between agents")
maxdistance = distance_between(agents[0], agents[1])
mindistance = maxdistance
for i in range(num_of_agents):
    for j in range(i, num_of_agents):# so does not repeat pairs.
         if i != j:#so agents do not test against themselves.
            distance = distance_between(agents[i], agents[j])
            maxDistance = max(maxdistance, distance)
            minDistance = min(mindistance, distance)
         
print("maxdistance=", maxDistance)
print("mindistance=", minDistance)
end = time.process_time()  
print("Time: ", end-start)