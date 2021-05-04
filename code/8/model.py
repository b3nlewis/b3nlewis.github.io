# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 11:05:18 2021

@author: b3nle
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework
import time
import csv
import random
from multiprocessing import Process
import argparse #used for commandline interface.

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
start_all = time.process_time()
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
environment = []     
agents = []
total = 0

carry_on = True
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])
ax.set_autoscale_on(True)

stopCond = random.randint(60,100) # Random stopping condition for stored units.
carry_on = True
print('Food Needed: ', stopCond)

end = time.process_time()
print('Step 1 Time : ', end-start)
    
'''
Step 2: Initialise model.
'''
start = time.process_time()

print("Step 2: Initialise model")

# Make the agents.
for i in range(num_of_agents):
    agents.append(agentframework.Agent(environment, agents, neighbourhood))

end = time.process_time()
print('Step 2 Time : ', end-start)
'''
Step 3: Generating functions.
'''
start = time.process_time()
print('Step 3: Generating update, gen_function, wait_fig and run animation functions')
def update(frame_number):
    '''
    This allows each agents to move, eat and share values.
    Agents are randomly shuffled each iteration.
    A stopping variable is created in this function. This is dependant
    on the stopping condition created in initialisation and the number of agents.
    This function is used in the update funcion which creates
    an animation in step 3.
    
    Parameters
    ----------
    frame_number:

    Returns
    -------
    Bool: Stopping Condition (True/False)
    Float: Agents x and y position each iteration.
    '''
    fig.clear()
    global carry_on
    global stopCond
    global total 
    random.shuffle(agents)# Randomly shuffles what order the agents move, eat and share.
    for i in range(num_of_agents):
        agents[i].move()
        agents[i].eat()
        #print(agents[i].store) 
        agents[i].share_with_neighbours(neighbourhood)
        total += agents[i].store
        #print('Store Total :',total)
    
    if total > (num_of_agents*stopCond):#Stopping condition based upon food stored.
        carry_on = False
        print("Stopping Condition Met")
    else:
        carry_on = True
         
    plt.imshow(environment)
    for i in range(num_of_agents):
        #plt.scatter(agents[i].x,agents[i].y)
        plt.scatter(agents[i].getx(),agents[i].gety())
    plt.show()
        
        
def gen_function(b = [0]):
    '''
    Provides a stopping variable for Matplotlib.animation.
    
    Returns
    -------
    int: a

    '''
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 100) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
          
    
def wait_fig(): 
    '''
    Function requires figure to remain open unitl all code has run and
    figure has shown all agent iterations.
        
    Returns
    -------
    Animation sequence.

    '''
    # Block the execution of the code until the figure is closed.
    # This works even with multiprocessing.
    if plt.isinteractive():
        plt.ioff() # this is necessary in mutliprocessing
        #plt.show(block=True)
        plt.show(block=False)
        plt.ion() # restitute the interractive state
    else:
        #plt.show(block=True)       
        plt.show(block=False)
    plt.pause(1)#closes figure automatically
    plt.close()
    return
end = time.process_time()
print('Step 3 Time : ', end-start)

def runAnimation():
    start = time.process_time()
    '''
    Function creates a figure based upon previous variables and functions by
    using the Matplotlib.animation module. The number of frames is calculated
    in the gen function.
    
    Parameters
    ----------
    fig: size of figure to be created.
    update: provides inputs to be displayed on figure
    gen_function: provides stoppping condition.

    Returns
    -------
    figure

    '''
    '''
    Step 4: Animating the graph to show each iteration.
    '''
    print("Step 4: Creating animation")
    animation = matplotlib.animation.FuncAnimation(fig, update, 
            repeat=False, frames=gen_function())#based on reasonable assumptions about food.
    #animation = matplotlib.animation.FuncAnimation(fig, update, 
            #repeat=False, frames=num_of_iterations)Displays all iteration steps.
    """Create animated plot. Continues to update the plot until stopping criteria is met.""" 
    plt.show()
    """Display the plot."""
    wait_fig()
    return
    
    end = time.process_time()
    print('Step 4 Time : ', end-start)

def main():
    '''
    Parameters
    ----------
    in.txt: Input environment raster
    HTML document: Provides agents starting position.
    
    Returns
    -------
    Environment Raster
    Agent starting locations for agentframework
    '''
    start = time.process_time()

    if __name__ != '__main__': return 
    
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
    plt.show()                     
    
    p = Process(target=runAnimation())
    p.start()
    #print('Animation Finished', flush = True) #just to have something printed here
    #p.join() # suppress this command if you want the animation be executed in
             # parallel with the subsequent code
    #for i in range(3): # This allows to see if execution takes place after the 
                      #process above, as should be the case because of p.join().
       #print('world', flush = True) 
       #time.sleep(1)
        
    plt.close()
    
    end = time.process_time()
    print('Animation Time : ', end-start)

    '''
    Step 5: Write out the environment as a .txt file
    '''
    start = time.process_time()
        
    print("Step 5: Exporting Environment")
    
    f2 = open('dataout.txt', 'w', newline='') 
    writer = csv.writer(f2, delimiter=',')
    for row in environment:		
    	writer.writerow(row)		# List of values.
    f2.close()
    
    end = time.process_time()
    print('Step 5 Time : ', end-start)
    
    '''
    Step 6: Writing total amount stored as a txt file
    '''
    
    start = time.process_time()
    
    print("Step 6: Exporting amount stored")
    print("Total store equals:", total)
    f3 = open('stored.txt', 'a') 
    f3.write(str(total) + '\n')		# Store Total and append to new line.
    f3.close()
    
    #Timing
    end = time.process_time()
    print('Step 6 Time : ', end-start)
    end_all = time.process_time()
    print("Total Time: ", end_all-start_all)
main()


