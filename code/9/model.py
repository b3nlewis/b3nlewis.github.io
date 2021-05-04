"""
# -*- coding: utf-8 -*-

Created on Tue Mar  2 11:05:18 2021

This is a program which generates an agent based model.
The model simulates sheep grazing in an environment.
Sheep (agents) can move, eat and share resources with other agents.
The program will finish when all agents have a randomly generated store value.
Requires agentframework.py to run.

@author: b3nle
"""
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation
import agentframework #self made class which processes movement, eating, storing and environment.
import time #measures time taken for processes
import csv
import random
import requests
from bs4 import BeautifulSoup
import tkinter
import sys
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
print("Step 1: Initialise Parameters")

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

#end = time.process_time()
print("Step 1 Completed")
#print('Step 1 Completed, Time : ', end-start)

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
    n = len(agents) #number of agents.
    for i in range(n):
        agents[i].move()
        agents[i].eat()
        #print(agents[i].store) 
        agents[i].share_with_neighbours(neighbourhood)
        total += agents[i].store
        #print('Store Total :',total)
    
    if total > (n*stopCond):#Stopping condition based upon food stored.
        carry_on = False #Stops program.
        print("Stopping Condition Met")
        print("Step 4 Completed. You can close the GUI, ethier by clicking exit model, or by closing the window.")
    else:
        carry_on = True
         
    plt.imshow(environment)#shows environment in gui.
    for i in range(n):
        #plt.scatter(agents[i].x,agents[i].y)
        plt.scatter(agents[i].getx(),agents[i].gety())
        #print(agents[i].getx, agent[i].gety)#python object
    #Remove plt.show() to get working in command line
    #plt.show() 
        
        
def gen_function():
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

animation = matplotlib.animation.FuncAnimation(fig, update, 
            repeat=False, frames=gen_function())#based on reasonable assumptions about food.

def runAnimation():
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

    '''Step 4: Animating the graph to show each iteration.'''
    print("Step 4: Creating animation for GUI")
    #start = time.process_time()
     
    global animation
    animation = matplotlib.animation.FuncAnimation(fig, update, 
            repeat=False, frames=gen_function())#based on reasonable assumptions about food.
    #animation = matplotlib.animation.FuncAnimation(fig, update, 
            #repeat=False, frames=num_of_iterations)Displays all iteration steps.
    """Create animated plot. Continues to update the plot until stopping criteria is met.""" 
    print('Showing Figure')
    plt.show()
    """Display the plot."""
    #print("Wait figure")#testing
    wait_fig()
    
    #end = time.process_time()
    #print('Step 4: Completed, Time : ', end-start)
    
    
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
    
    if __name__ != '__main__': return
    
    '''Step 2:Reading in environment'''
    print("Step 2: Reading in Environment from in.txt")
    #start = time.process_time()
    
    with open('in.txt', newline='') as f:
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
    '''#plt.show() Does not work in cmd'''

    #end = time.process_time()
    print("Step 2 Completed")
    #print('Step 2 Time : ', end-start)

    '''Step 3: Calculating agents from HTML document'''
    print("Step 3: Creating Agents")
    #start = time.process_time()
    
    #Get agents x and y from html document.
    r = requests.get('https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    #print(content)
    table = BeautifulSoup(content, 'html.parser')#gets html document and parses text into python variable to use later on.
    #print(table)
    
    y_table = table.find_all(attrs={"class" : "y"})#finds all tages with the class attribute "y" and "x", removes "z".
    x_table = table.find_all(attrs={"class" : "x"})
    #print(y_table)
    #print(x_table)
    print(len(y_table),"model coordinates collected from HTML table")
    
    # Make the agents.
    for i in range(num_of_agents):
        y = int(y_table[i].text)
        x = int(x_table[i].text)
        agents.append(agentframework.Agent(environment, agents, neighbourhood, y, x))
        #print(y,x) 

    #end = time.process_time()
    print("Step 3 Completed")                  
    #print('Step 3 Time : ', end-start)

    


# The process is quit as well as destroying the main window (root) on exit
def exiting():
    '''
    When GUI is closed, this function stops the program.
    It outputs the environment and total units stored to txt files.
    It also checks to see if the program ran correctly checking the total
    units stored meets the store requirements.
    
    Parameters
    ----------
   
    Environment Raster
    total: total stored units for all agents.

    Returns
    -------
    dataout.txt: environment 
    stored.txt: total stored units.
    '''
    
    root.quit()
    root.destroy()
    
    '''Step 5: Write out the environment as a .txt file'''
    print("Step 5: Exporting Environment to dataout.txt")
    #start = time.process_time()    
    
   
    f2 = open('dataout.txt', 'w', newline='') 
    writer = csv.writer(f2, delimiter=',')
    for row in environment:		
    	writer.writerow(row)		# List of values.
    f2.close()
   
    #end = time.process_time()
    print("Step 5 Completed")
    #print('Step 5 Time : ', end-start)
   
    
    '''Step 6: Writing total amount stored as a txt file'''
    print("Step 6: Exporting amount stored to stored.txt")
    #start = time.process_time()
   
    print("Total store equals:", total)
    f3 = open('stored.txt', 'a') 
    f3.write(str(total) + '\n')		# Store Total and append to new line.
    f3.close()
      
    #end = time.process_time()
    print("Step 6 Completed")
    #print('Step 6 Time : ', end-start)
    
    
    '''Step 7: Checking Results'''
    print("Step 7: Checking Results")
    #start = time.process_time()
    
    checking_results = num_of_agents * stopCond #Calculates if the agents have stored enough food based upon previous parameters.
    if checking_results <= total:
        print("The agents have met the stored requirements, the requirement was:", str(checking_results))
    else:
        print("Agent model has failed, stored requirements not met, the requirement was:", str(checking_results))
        
    #end = time.process_time()
    print("Step 7 Completed")
    #print('Step 7 Time : ', end-start)
    end_all = time.process_time()
    tt = end_all-start_all
    print("Operation time was",tt , "seconds")
    
    f4 = open('time.txt', 'a')#adding time to file so can be checked. 
    f4.write(str(tt) + '\n')		# Time Total and append to new line.
    f4.close()
    #sys.exit()#forces system to exit
    
# Initial GUI set up
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=runAnimation)
model_menu.add_command(label="Exit model", command=exiting)
  
main()#When run model is pressed on GUI main function starts   
root.protocol('WM_DELETE_WINDOW', exiting)#When the GUI window is closed the exiting function is run.
tkinter.mainloop()#GUI is constantly checking if it has been clicked.

