#import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
#the total population: make array of all susceptible population(0=susceptible, 1=infected, 3=recovered)
population=np.zeros((100,100))
#infection probability(beta) and recovery probability(gamma)
beta=0.3
gamma=0.05
#get an array as a random coordinate in the array 'population', which means 1 random person
outbreak=np.random.choice(range(100),2)
#make this person infected
population[outbreak[0],outbreak[1]]=1
def spatial(timepoint):
    #repeat for 100 times:
    #neighbourhoods of the infected indiviuals have a probability of beta to be infected
    #infected individuals have a probability of gamma to recover
    for i in range(0,timepoint):
        #find the infected individuals
        infected=np.where(population==1)
        #infected individual may recover(2='should recover')
        # loop through all infected points
        for i in range(len(infected[0])):
            # get x, y(a, b) coordinates for each point
            a= infected[0][i]
            b= infected[1][i]
            #only infected individuals may recover
            if population[a,b]==1:
                population[a,b]=np.random.choice([1,2],1,p=[1-gamma,gamma])[0]
        #neibourhoods of infected may be infected
        infected=np.where((population==1)|(population==2))
        # loop through all infected points
        for i in range(len(infected[0])):
            # get x, y coordinates for each point
            x = infected[0][i]
            y = infected[1][i]
            # infect each neighbour with probability beta
            # infect all 8 neighbours (this is a bit finicky, is there a better way?):
            for xNeighbour in range(x-1,x+2):
                for yNeighbour in range(y-1,y+2):
                    # don't infect yourself! (Is this strictly necessary?)
                    if (xNeighbour,yNeighbour) != (x,y):
                        # make sure I don't fall off an edge
                        if xNeighbour != -1 and yNeighbour != -1 and xNeighbour!=100 and yNeighbour!=100:
                            # only infect neighbours that are not already infected!
                            if population[xNeighbour,yNeighbour]==0:
                                population[xNeighbour,yNeighbour]=np.random.choice(range(2),1,p=[1-beta,beta])[0]
        #make the recovered not taking part in further programme
        recovered=np.where(population==2)
        for i in range(len(recovered[0])):
            c=recovered[0][i]
            d=recovered[1][i]
            population[c,d]=3
    plt.figure(figsize=(6,4),dpi=150)
    plt.imshow(population,cmap='viridis',interpolation='nearest')
    plt.show()
    return()
#plot the result
spatial(0)
spatial(10)
spatial(50)
spatial(100)
