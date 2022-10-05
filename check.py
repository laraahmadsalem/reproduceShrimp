#
# Author : Lara Ahmad Salem
# ID : 19491787
#
# check.py - Handles most of the checking and validation and supports functions for the simulation  
#
# Revisions: 
#
# 10/10/2019 – Intial Version 
# 27/10/2019 - Slight modifications to check collision 

import random
import matplotlib.pyplot as plt
import numpy as np
import time
from shrimp import Shrimp

def checkCollision(shrimpList, shrimp):
    """ A function that checks the coordinates between two shrimps and detects whether they can reproduce 
        Argument: shrimpList - contains all the shrimps to test by 
                  shrimp - a single shrimp object 
    """
    #retrieves the coordinates of the shrimp we want to check for
    x = shrimp.pos[0]
    y = shrimp.pos[1] 
    # sets initial collision to no 
    collided = "no"

    #looping through entire shrimp list and checking against the other shrimps coordinates
    for n in shrimpList:
        if(n is not shrimp): #check to see they arent the same shrimp 
            if(n.pos[0] == x and n.pos[1] == y):  #if both coordinates match
              
                #confirm the gender of both shrimps and their state (make sure they are both adults)
                result = checkGender(n,shrimp)
                result2 = checkState(n,shrimp) 
              
                #if they are both adults and opposite genders then they can mate
                if(result == True and result2 == True):
                    collided = "adults_and_can_mate"
                else: 
                    collided = "cannot_mate"

                n.collideChange()
                shrimp.collideChange() 
                # after they collide they change direction 
    return collided 

def checkGender(n,shrimp):
    """ A function that checks the genders of two shrimps to make sure they are opposite before they can mate 
        Argument: n - shrimp number 1
                  shrimp - the second shrimp object 
    """    
    canmate = False 
    if(n.gender != shrimp.gender):
        canmate = True
    return canmate

def checkState(n,shrimp):
    """ A function that makes sure both shrimps are adults
        Argument: n - shrimp number 1
                  shrimp - the second shrimp object 
    """  
    areadults = False 
    if(n.state == "adult" and shrimp.state == "adult"):
        areadults = True 
    return areadults

def validCoordinates (x,y):
    """ A function that ensures both the x and y coordinates are greater than 0  
        Argument: x - integer x coordinates
                  y - integer y coordinates  
    """  
    if (x>0 and y>0):
        return True 
    else: 
       raise ValueError("The Values of X and Y cannot be negative") 
    
def validPositive (value): 
    """ A Generic function that checks to see the value passed in is greater than 0  
        Argument: value - integer 
                  
    """
    if(value>0):
        return True
    else: 
        raise ValueError("The value cannot be negative") 

