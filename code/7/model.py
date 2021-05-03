# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:05:18 2021

@author: b3nle
"""
import matplotlib.pyplot as plt
import agentframework
import time
import csv
import random
import argparse

#Commandline interface
parser = argparse.ArgumentParser(description=
'Run an agent based model for sheep. Defaults are available for variables')

parser.add_argument('-a', '--agents', type=int, metavar = '', help='Number of agents in model')
parser.add_argument('-i', '--iterations', type=int, metavar = '', help='Number of iterations in model')
parser.add_argument('-n', '--neighbourhood', type=int, metavar = '', help='Neighbourhood of agents')
args = parser.parse_args()

'''
Step 1: Initialise Parameters
'''
start = time.process_time()
print("Step 1: Initialise Parameters, read data and show environment")

#sets arguments to defaults if not inputted in command line.
if args.agents == None:
    num_of_agents = 50
else:
    num_of_agents = args.agents
    
if args.iterations == None:
    num_of_iterations = 20
else:
    num_of_iterations = args.iterations
    
if args.neighbourhood == None:
    neighbourhood = 20
else:
    neighbourhood = args.neighbourhood
    
print('Agents:', num_of_agents)
print('Iterations:', num_of_iterations)
print('Neighbourhood:', neighbourhood)

environment = [] #creates empty list for environment    
agents = [] #creates empty list for environment


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
print("To continue close plot")
plt.show()


'''
Step 2: Initialise agents.
'''
print("Step 2: Initialise agents")
# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))

'''
Step 3: Move agents using move method from agentframework.
'''
print("Step 3: Move agents using move, eat and share methods from agentframework")
# Move the agents.
for j in range(num_of_iterations):
    random.shuffle(agents)# Randomly shuffles what order the agents move, eat and share.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
        
'''
Step 4: Create a graph showing results.
'''
print("Step 4: Create a graph showing results")
plt.xlim(0, 300)
plt.ylim(0, 300)
plt.imshow(environment)
print("To continue close plot")
for i in range(num_of_agents):
    plt.scatter(agents[i].x,agents[i].y)
plt.show()

'''
Step 5: Write out the environment as a .txt file
'''
print("Step 5: Writing environment in txt file")

f2 = open('dataout.txt', 'w', newline='') 
writer = csv.writer(f2, delimiter=',')
for row in environment:		
	writer.writerow(row)		# List of values.
f2.close()

'''
Step 6: Writing total amount stored as a txt file
'''
print("Step 6: Writing total amount stored as a txt file")
total = 0
for i in range(num_of_agents):
    total += agents[i].store
print("Total store equals:", total)
f3 = open('stored.txt', 'a') 
f3.write(str(total) + '\n')		# Store Total and append to new line.
f3.close()

end = time.process_time()  
print("Time: ", end-start)