# -*- coding: utf-8 -*-
"""
A basic Agent Based Model, which creates two agents 
in random locations within a 100x100 grid and moves
them randomly three times.

@author: b3nle
"""

#Modules
import random

# Create first set of variables.
y0 = random.randint(0,99)#creates variables in random location.
x0 = random.randint(0,99)

#Change y and x randomly, first time.
if random.random() < 0.5:
    y0 += 1
else: 
    y0 -= 1
if random.random() < 0.5:
    x0 += 1
else: 
    x0 -= 1
    
#Change y and x randomly, second time.
if random.random() < 0.5:
    y0 += 1
else: 
    y0 -= 1
if random.random() < 0.5:
    x0 += 1
else: 
    x0 -= 1
    
#Change y and x randomly, third time.
if random.random() < 0.5:
    y0 += 1
else: 
    y0 -= 1
if random.random() < 0.5:
    x0 += 1
else: 
    x0 -= 1


# Create second set of variables.
y1 = random.randint(0,99)
x1 = random.randint(0,99)

#Change y and x randomly, first time.
if random.random() < 0.5:
    y1 += 1
else: 
    y1 -= 1
if random.random() < 0.5:
    x1 += 1
else: 
    x1 -= 1
    
#Change y and x randomly, second time.
if random.random() < 0.5:
    y1 += 1
else: 
    y1 -= 1
if random.random() < 0.5:
    x1 += 1
else: 
    x1 -= 1
    
#Change y and x randomly, third time.
if random.random() < 0.5:
    y1 += 1
else: 
    y1 -= 1
if random.random() < 0.5:
    x1 += 1
else: 
    x1 -= 1
    
    
#Work out euclidean distance between two sets of y and xs.
answer = (((y0 - y1)**2) + ((x0 -x1)**2))**0.5
print(answer)