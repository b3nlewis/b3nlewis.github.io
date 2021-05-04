# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:05:18 2021

This model adds inputs and outputs to provide additional functionallity and
context to the model and results.

@author: b3nle
"""

import matplotlib.pyplot as plt
import agentframework
import time
import csv

'''
Functions
'''
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
print("Step 1: Initialise Parameters, read data and show environment")
num_of_agents = 100
num_of_iterations = 100
environment = []     
agents = []

f = open('in.txt', newline='') 
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:				# A list of rows
    rowlist = []                # An empty list
    for value in row:			# A list of value
        rowlist.append(int(value))   # Append values to rowlist
    environment.append(rowlist) # Append rowlist to environment 
f.close() 	# Don't close until you are done with the reader;
		# the data is read on request.
        
# create graph to show data
plt.imshow(environment)
print("Close Graph")
plt.show()


'''
Step 2: Initialise agents.
'''
print("Step 2: Initialise agents")
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment))

'''
Step 3: Move agents using move method from agentframework.
'''
print("Step 3: Move agents using move method from agentframework")
# Move the agents.
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        
'''
Step 4: Create a graph showing results.
'''
print("Step 4: Create a graph showing results")
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.imshow(environment)
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
print("Close Graph")
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

'''
Step 6: Write out the environment as a .txt file
'''
print("Step 6: Writing environment in txt file")

f2 = open('dataout.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

'''
Step 7: Writing total amount stored as a txt file
'''
print("Step 7: Writing total amount stored as a txt file")
total = 0
for i in range(num_of_agents):
    total += agents[i].store
print("Total store equals:", total)
f3 = open('stored.txt', 'a') 
f3.write(str(total) + '\n')		# Store Total and append to new line.
f3.close()

end = time.process_time()  
print("Time: ", end-start)