#
# Author : Lara Ahmad Salem
# ID : 19491787
#
# fileIO.py - Deals with the Input and Output of the simulation 
#
# Revisions: 
#
# 27/10/2019 – Creation of Functions

import random
import matplotlib.pyplot as plt
import numpy as np
import time
from userInput import * 
from shrimp import Shrimp

def readInput(f):
    """ A fileIO function that reads an input file to retrieve the parametres to run the simulation  
        Argument: f - a file pointer to read data 
                    
    """
    try:
        #reads each line from the file and retrieves maximum x,y and the population as well as the timestep 
        xmax = int(f.readline())
        ymax = int(f.readline())
        pop = int(f.readline())
        timeS = int(f.readline())
        #validates that the parametres are all valid 
        if((validCoordinates(xmax,ymax)) and (validPositive (pop)) and (validPositive(timeS))):
          #if they are valid then append to an array and return to construct the simulation   
          values = [xmax,ymax,pop,timeS]
          return values
        else: 
            raise ValueError("The value cannot be negative")
        
        f.close() 
        #close the file 
    except ValueError: 
        print("Values are Invalid")

def output2file (shrimp):
    """ A function that checks to see whether a user would like their shrimps outputted to a file   
        Argument: shrimp - list of shrimp objects  
    """
    try: 
        #checks to see whether a user is interested in writing out to a file 
        choice = int(input("\nPress (1) to Output results to a File \n(2) to Return \n "))
        if(choice==1):
            try: 
                #if the user wants to output to a file then we can retrieve the file name
                fileName = input("\nPlease enter the name of the file you would like to save the Shrimps to...\n")
                #open the file 
                fileN = open(fileName,"w")
                #output the filename and shrimp list to be written out to a file 
                write2file(fileN,shrimp)
            except IOError: 
                #if any I/O errors occur they are encapsulated in a try-catch 
                print("File doesn't exist")
        elif(choice==2):
            print("Now Exiting the program")
        else:
            print("Invalid Selection from the Options Above")
    except ValueError: 
        print("Invalid Selection from the Options Above")

def write2file (fileName,shrimp):
    """ A simple function that writes out teh shrimp objects to a file   
        Argument: fileName - file pointer of the file to write out to 
                  shrimp - list of shrimp objects 
    """
    try:
        #loop through the shrimp objects one by one  
        for n in shrimp: 
            #write out every shrimp object to a new line with its inbuilt string function 
            fileName.write("\n" + str(n))
        #once done the file stream will be closed 
        fileName.close() 
    except IOError: 
        print("Error Writing to the file")