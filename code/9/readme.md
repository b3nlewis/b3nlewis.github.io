# Readme
This readme file will give an overview of the agent based model, what is does and the associated files.

## Overview
The ABM allows agents (sheep) to interact with the environment and each other. Agents are placed randomly in the starting environment, each update the agents move randomly one unit,
eat the environment and prescribed amount, and if within range of other agents share food. Additionally, the agents have a random chance of sicking up food units which then adds to
the environment. The model continues to run until the stopping condition is met. The stopping condition is based on a randomly generated food total (between 60 and 100) and the number
of agents. When all of the agents meet the food total the program stops. When exiting the program, the environment, food stored and time completion are exported to txt files.

## Associated files
Input: in
      A txt file with values which range between 0 and 255. This is the environment and the agents eat this.
      
Output: dataout
      This is the environment after the model has completed. It will be altered due to agents eating it.
Output: store
      This is the total amount of food units stored by all agents. 
Output: time
      Records how long the script takes to complete. Normally takes between 3 to 4 seconds.
      
## How to use
This script can be run in IDLE or command line. Using the command line is recommended as variables (number of agents, number of iterations and neighbourhood size) can be changed.
Varaibles are optional and defaults of 50, 20, 20 are set. In order to use command line type "python model.py -h" to bring up help information.
