# Agent Based Model Practicals

This repositry contains all of the work I have completed for GEOG5990.
There were nine practicals in this course and there are links to all nine folders with all of the necessary code contained.
The nine practicals get more complex with practical nine being the final product. Read the documentation before using.

### Practical 1
A simple agent based model, where two points randomly move around a space and the distance between them is calculated.

### Practical 2
The agents are added and created in a list to shrink the code.

### Practical 3
For loops are added to create multiple agents and move them multiple time throughout the map. A torus boundary effect is added to keep agents in one space.

### Practical 4
A function is added to calculate the distance between all agents which can be accessed throughout the script.

### Practical 5
The script is converted into an object-oriented version where agents have properties and behaviours stored in a separate script, agentframework.

### Practical 6
Inputs and outputs are added to the code, which store information about the environment and how much food is eaten.

### Practical 7
Agentframework is altered to allow agents to share food with each other based upon a distance variable.

### Practical 8
The model is now animated in a separate window. The animation is dependant on a stopping condition. This condition is a random based food value, when every agent reaches this value the script stops.

### Practical 9
A GUI was added to run and exit the script. Additional help information was added to the command line.

## Running the model
Before running the model in command line type: "python model.py -h".
This will display additional information to help you run the model. The model can be run without any additional parameters added as there are defaults. However, arguments can be added using -a, -i, -n. A GUI will appear, click run in the menu bar. The model will run. When it is completed the command line will tell you when you can exit the model. On exit, data will be exported in txt files.
