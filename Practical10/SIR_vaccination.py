#import libraries
import numpy as np
import matplotlib.pyplot as plt
#total population
N=10000
#define the function which is a SIR model with vaccination
def SIR(vaccinated):
    #each populations(at the beginning)
    susceptible=9999-vaccinated
    infected=1
    recovered=0
    #infection probability(beta) and recovery probability(gamma)
    beta=0.3
    gamma=0.05
    #array for tracking
    infected_record=[infected]
    #repeat for 1000 times:
    #each susceptible individual has a beta*(the infected proportion) probability to become infected
    #each infected individual has a gamma probability to become recovered
    #record infected population every time point in the array
    for i in range(0,1000):
        susceptible_infected_list=list(np.random.choice(range(2),susceptible,p=[beta*infected/N,1-beta*infected/N]))
        infected_recovered_list=list(np.random.choice(range(2),infected,p=[gamma,1-gamma]))
        susceptible=susceptible_infected_list.count(1)
        infected=susceptible_infected_list.count(0)+infected_recovered_list.count(1)
        recovered=infected_recovered_list.count(0)+recovered
        #record
        infected_record.append(infected)
    #return the array
    return(infected_record)
#get the data and plot the result
plt.figure(figsize=(6,4),dpi=150)
plt.plot(SIR(0),label='0%')
plt.plot(SIR(1000),label='10%')
plt.plot(SIR(2000),label='20%')
plt.plot(SIR(3000),label='30%')
plt.plot(SIR(4000),label='40%')
plt.plot(SIR(5000),label='50%')
plt.plot(SIR(6000),label='60%')
plt.plot(SIR(7000),label='70%')
plt.plot(SIR(8000),label='80%')
plt.plot(SIR(9000),label='90%')
plt.plot(SIR(9999),label='100%')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()