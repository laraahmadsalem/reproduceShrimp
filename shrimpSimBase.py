#
# Author : Lara Ahmad Salem
# ID : 19491787
#
# shrimpSimBase.py - Basic simulation of brine shrimp for assignment, S2 2019. 
#
# Revisions: 
#
# 2/10/2019 – Base version for assignment
# 10/10/2019 - Creates Shrimp   
# 12/10/2019 - added the while loop
# 15/10/2019 - separated a main function and the simulation into submodules 

import random
import shrimp
import matplotlib.pyplot as plt
import numpy as np
import time
import sys 
from fileIO import * 
from shrimp import Shrimp
def main():
    
    #to get random simulation each time
    random.seed()

    if(len(sys.argv) == 5):
        #testing to see if we have 5 parametres 
        if(validCoordinates(int(sys.argv[1]),int(sys.argv[2])) and validPositive (int(sys.argv[3])) and validPositive(int(sys.argv[4]))):
            XMAX = int(sys.argv[1]) 
            YMAX = int(sys.argv[2])
            POPULATION = int(sys.argv[3])
            TIMESTEP = int(sys.argv[4])
            #if all values are valid then we proceed to assign them to the variables 
        else: 
            #default values being set if values are invalid 
            print("Values are invalid, now being run with default values")
            XMAX = 100
            YMAX = 100
            POPULATION = 200 
            TIMESTEP = 20 
     
        # values are sent to be simulated 
        shrimp = Simulator(XMAX,YMAX,POPULATION,TIMESTEP)
        #shrimp list is returned and user can output to a file 
        output2file(shrimp)

    elif (len(sys.argv) == 1):
        #if no parametres are present the program will run with default values 
        option = welcome()
        # welcome banner displayed to welcome users 
        if(option == 1):
            print("STARTING SIMULATION..........")
            #default values are being assigned and sent to the simulation function 
            XMAX = 100
            YMAX = 100
            POPULATION = 200 
            TIMESTEP = 20 
            shrimp = Simulator(XMAX,YMAX,POPULATION,TIMESTEP)   
            output2file(shrimp)     
        elif(option == 2):
            #if a user wants to know how to run with command line parametres they select this option 
            CommandLineUsage()
        elif(option == 3):
            #if a user wants to know how to run by using file input they select this option 
            CommandLineUsageFile()
        else:
            #if no option matches throw a print statement 
            print("Option Not Valid")

    elif (len(sys.argv) == 3):
        #if 3 command line parametres are present then we will be running the simulation with file I/O 
        try:
            #open both the input and output file 
            #these are encapsulated with a try catch to ensure that files exist 
            f = open(sys.argv[1],"r")
            w = open(sys.argv[2],"w")
            # file will then read parametres and ensure they are valid 
            values = readInput(f)
            #sent off to be simulated 
            shrimp = Simulator(values[0],values[1],values[2],values[3])
            #outputted to a file 
            write2file(w,shrimp) 
        except IOError:
            print ('Cannot Open File')
    else:
        print("Input Parametres are Invalid")
        

def Simulator(XMAX,YMAX,POPULATION,TIMESTEP):
    """ Main function that creates the shrimps and simulates the lifecycle   
        Argument: XMAX - maximum x value of scatter plot
                  YMAX - maximum y value of scatter plot 
                  POPULATION - number of shrimps that need to created for simulation 
                  TIMESTEP - how many times we need to simulate the shrimps  
    """
    # a list of shrimp objects 
    shrimp = []
    #loop until we reach population and create the shrimps 
    for i in range(POPULATION):
        #assigned random coordinates in the scatter plot 
        randX = random.randint(0,XMAX)
        randY = random.randint(0,YMAX)
        # gender is generated randomly to ensure unbias data 
        gender = random.randint(0,1)
        # shrimps are then appended to the list 
        shrimp.append(Shrimp([randX,randY],gender))
        # the first shrimps released into the water are diaplayed 
        print(shrimp[i])
    
    #iterate through the timestep displaying the shrimps  moving, reproducing or dying 
    for i in range(TIMESTEP):
        print("\n ### TIMESTEP ",i, "###")
        plt.cla()
        # x,y,sizes and colours lists are created to be plotted and displayed on the screen 
        xvalues = []
        yvalues = []
        sizes = []
        colours = []
        m = 0 

        #ensures that the loop through entire list even when appending a new shrimp 
        while m < len(shrimp):

            #random value created to check death probability 
            rnd = random.random()
            #changes movement each timestep for each shrimp 
            shrimp[m].stepChange(rnd,XMAX,YMAX)
            print(shrimp[m])
            #append all relevant informaion for the shrimp to be displayed in the plot 
            xvalues.append(shrimp[m].pos[0])
            yvalues.append(shrimp[m].pos[1])
            sizes.append(shrimp[m].getSize())
            colours.append(shrimp[m].getColor())

            #check each current shrimp by all the shrimps to detect if they collide and can mate 
            collided = checkCollision(shrimp,shrimp[m])
            
            #if both conditions are met then we create a new baby brine shrimp egg that will be created in 
            #the collided spot 
            if(collided == "adults_and_can_mate"):
                #assign the coordinates 
                gender = random.randint(0,1) 
                randX = random.randint(1,XMAX)
                randY = random.randint(1,YMAX)
                #append new shrimp to list 
                shrimp.append(Shrimp([randX,randY],gender))

            m += 1
       
        
        plt.scatter(xvalues, yvalues, s=sizes,c=colours)   # Note plt origin is bottom left 
        plt.xlim(0,XMAX)
        plt.ylim(0,YMAX)
        plt.pause(0.2)
        #plt.show()
        #time.sleep(2) 
    plt.show()

    return shrimp
  
if __name__ == "__main__":
    main()
