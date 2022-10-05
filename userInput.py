#                                                                               
# Author : Lara Ahmad Salem                                                     
# ID : 19491787                                                                 
#                                                                               
# userInput.py - Handles most of the Output to the Screen for users  
#                                                                               
# Revisions:                                                                    
#                                                                              
# 22/10/2019 – Initial Version                                        
#                                                                               

import random                                                                   
import matplotlib.pyplot as plt                                                 
import numpy as np                                                              
import time                                                                     
import sys                                                                      
from matplotlib.offsetbox import OffsetImage, AnnotationBbox                    
from shrimp import Shrimp                                                       
from check import *              


def welcome ():
    """ Prints out welcome message for users and provides information on different methods to use simulation 
        Argument: N/A 
    """
    option = 0 
    print("==================================================")
    print("|      WELCOME TO THE SHRIMP SIMULATION PROGRAM   | ")
    print("==================================================")
    print("|  This program is being run with default values  | ")
    print("| To Customise Values please re-run the program   |")
    print("==================================================")
    print("|   Default Values are :-                         |")
    print("| (1) Maximum X Value:- 100                       |")
    print("| (2) Maximum Y Value:- 100                       |")
    print("| (3) Total Number of the Shrimp Population:- 200 |")
    print("| (4) Default Time Step:- 20                      | ")
    print("==================================================")
    try:
            option = int(input("To Begin this Simulation: \n Press (1) to run with default values \n Press (2) For more information to customise your simulation \n Press (3) For more information on reading in from a File\n "))
    except ValueError: 
            print("Cannot Input Characters or Strings")        

    
    return option 

def CommandLineUsage ():
    """ Prints out the command line parametres required to run the program and where they should go 
        Argument: N/A 
    """
    print("========================================================================================================")
    print("| To Use this Simulation with command line Arguments Re-run the program with the following parametres  |")
    print("| python3 shrimpSimBase.py <XMAX> <YMAX> <POPULATION> <TIMESTEP>                                       | ") 
    print("========================================================================================================")                                                    
                                                    
def CommandLineUsageFile (): 
    """ Advises users on how to use the program if they would like to read in the parametres from a file and output to a text file
        Argument: N/A 
    """
    print("========================================================================================================")
    print("| To Use this Simulation by reading in from a file, Re-run the program with the following parametres  |")
    print("| python3 shrimpSimBase.py <FILENAME> <OUTPUTFILE>                                                                |")
    print("| File should be formatted as folows:                                                                 |") 
    print("| <XMAX>                                                                                              |")  
    print("| <YMAX>                                                                                              |")      
    print("| <POPULATION>                                                                                        |")                                                                       
    print("| <TIMESTEP>                                                                                          |")                                       
    print("========================================================================================================")                                                    
                                                        
                                                    


                                                    
                                                    
                                                    
                                                    
                                                    
                                                                        
