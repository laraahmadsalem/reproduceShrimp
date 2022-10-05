#
# Author : Lara Ahmad Salem 
# ID : 19491787 
#
# shrimp.py - Class definitions for simulation of brine shrimp 
#
# Revisions: 
#
# 2/10/2019 – Base version for assignment
# 10/10/2019 - Added new functions for updating the state of the shrimp 
# 12/20/2019 - collision change function 

import random 


class Shrimp():
    # Scientific paper states it takes brine shrimp eggs 24-36 hours to hatch 
    time2hatch = 3
    # 5 different states of a shrimp based on the brine shrimps lifecycle 
    states = ["egg","hatchling","larvae","juvenile","adult","dead"]
    # Gender of brine shrimp, determined by random probability, if 0 then male if 1 then female 
    genders = ["male","female"]   
    # probability that a shrimp will die increases as they age as based on research paper  
    deathprob = {"egg":0.01, "hatchling":0.02,"larvae":0.03,"juvenile":0.04,"adult":0.05}
    # image = pygame.image.load('egg.jpeg')


    def __init__(self, pos, ii):
        self.pos = pos
        self.state = self.states[0]
        # all shrimps start out as eggs 
        self.age =  0
        #assigns a gender to the shrimp based on a value of 1 or 0 
        self.gender = self.genders[ii]
        
    def __str__(self):
        #string function that prints out a string representation of the Object 
        return self.state + " @ " + str(self.pos) + " Gender " + str(self.gender) 
    
    def updateState(self):
        """ Updates state of a brine shrimp depending on age
        Argument: age - the age of the shrimp 
        """
        # Please note: The ages used here are not an accurate representation of real life shrimp
        #              and are for experimental purposes to generate a simulation of the lifecycle 
    
        if self.age < 1: 
            self.state = "egg"
        elif self.age > 1 and self.age <= 2:
            self.state = "hatchling"
        elif self.age > 2 and self.age <= 4:
            self.state = "larvae"
        elif self.age > 6 and self.age <= 7: 
            self.state = "juvenile"
        elif self.age >= 7: 
            self.state = "adult"

    def collideChange(self): 
        """ Changes the position of a shrimp if it has collide with another shrimp.
        Argument: self 
        """
        if self.state != "dead":
            rnd = random.random() 
            #random number of probability to calculate death probability 
            if rnd < self.deathprob[self.state]:
                self.state = "dead"
                #once a brine shrimps state is "dead" they will move to the bottom of the sea
                self.pos[1] = 0

            else:
                #random value between 0 and 30 to move shrimp if it has collided 
                rand = random.randint(0,30)  

                if self.state == "egg":
                    self.pos[0] 
                    self.pos[1] -= rand
                elif self.state == "hatchling":
                    self.pos[0] += rand 
                    self.pos[1] += rand
                elif self.state == "larve":
                    self.pos[0] += rand 
                    self.pos[1] += rand 
                elif self.state == "juvenile":
                    self.pos[0] += rand 
                    self.pos[1] += rand
                elif self.state == "adult":
                    self.pos[0] += rand 
                    self.pos[1] += rand
                
    def boundaryCheck(self,maxX,maxY):
        """ Checks the boundaries of the coordinates of the Shrimp
        Argument: self - object shrimp  
                  maxX - maximum boundary of scatter plot for X coordinates 
                  maxY - maximum boundary of scatter plot for Y coordinates 
        """  
        if(self.pos[0] > maxX):  
            # if greater than boundary then adjust to a different value and decrease x value by random number 
            self.pos[0] = (maxX - 30) 
            self.pos[0] -= random.randint(1,30)

        elif(self.pos[0] < 0):
            # if less than boundary then adjust to a different value and increase x value by random number 
            self.pos[0] =  (maxX - 30) 
            self.pos[0] += random.randint(1,30)  

        if(self.pos[1] > maxY):
            self.pos[1] -= random.randint(1,30)
            
        elif(self.pos[1] < 0): 
            self.pos[1] += random.randint(1,30)
          
    

    def stepChange(self,rnd,XMAX,YMAX):
        """ Shrimp coordinates are changed everytime this function is called 
        Argument: self - object shrimp 
                  rnd - random value used to calculate death probability 
                  XMAX - maximum x value for coordinates 
                  YMAX - maximum y value for coordinates 
        """
        #Note: The steps that the shrimps moves are based on random probability 
        #      the older it gets the more chances it can move faster and cover 
        #      more space. This is in no way accurate to real life shrimps, only 
        #      a simulation. 
        if self.state != "dead":
            if rnd < self.deathprob[self.state]:
                self.state = "dead"
                #once a brine shrimps state is "dead" they will move to the bottom of the sea
                self.pos[1] = 0

            else:
                self.age += 1
                self.updateState() 
                rand = random.randint(0,1) 
                # uses random probability to determine whether to change direction at some point 
                # 1 will indicate positive and continue move forward 
                # 0 will indicate a shift in direction 

                if self.state == "egg" and rand == 1:
                    self.pos[0] += random.randint(1,5) 
                    self.pos[1] += random.randint(1,10) 
                    #the younger the state the slower the shrimp will move 
                elif self.state == "hatchling" and rand == 1:
                    self.pos[0] += random.randint(1,10) 
                    self.pos[1] += random.randint(1,5)
                elif self.state == "larve" and rand == 1:
                    self.pos[0] += random.randint(1,20) 
                    self.pos[1] += random.randint(1,10) 
                    #as the shrimp ages there is a greater chance it will move faster 
                    #and greater distances 
                elif self.state == "juvenile" and rand == 1:
                    self.pos[0] += random.randint(1,30)  
                    self.pos[1] += random.randint(1,20) 
                elif self.state == "adult" and rand == 1:
                    self.pos[0] += random.randint(1,40) 
                    self.pos[1] += random.randint(1,30) 
                else: 
                    self.pos[0] -= random.randint(1,10) 
                    self.pos[1] -= random.randint(1,10)

            self.boundaryCheck(XMAX,YMAX)
            #makes sure that none of the shrimps get out of bounds 
    
    def getSize(m):
        """ Retrieves the Size of the shrimp depending on state.
        Argument: m - the object shrimp 
        """
        #based on a research paper i have ensured that the shrimps are not to scale 
        # size. 
        if m.state == "egg":
            size = 1
        elif m.state == "hatchling":
            size = 2
        elif m.state == "larvae":
            size = 4
        elif m.state == "juvenile":
            size = 6
        elif m.state == "adult":
            size = 7
        else: 
            size = 7
        # assume that the size will be defualt adult (will fix later)
        return size

    def getColor(m):
        """ Retrieves the colour of the shrimp depending on state.
        Argument: m - the object shrimp 
        """
        #depending on age of the shrimp it will be displayed in a different colour 
        if m.state == "egg":
            colour = "y"
        elif m.state == "hatchling":
            colour = "purple"
        elif m.state == "larvae":
            colour = "crimson"
        elif m.state == "juvenile":
            colour = "green"
        elif m.state == "adult" and m.gender == "female":
            colour = "orange"
        elif m.state == "adult" and m.gender == "male":
            colour = "blue"
        else: 
            colour = "maroon"
        return colour
