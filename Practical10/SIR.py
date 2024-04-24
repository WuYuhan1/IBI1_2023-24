#import libraries
import numpy as np
import matplotlib.pyplot as plt
#each populations(at the beginning)
susceptible=9999
infected=1
recovered=0
#total population
N=susceptible+infected+recovered
#infection probability(beta) and recovery probability(gamma)
beta=0.3
gamma=0.05
#arrays for tracking
susceptible_record=[susceptible]
infected_record=[infected]
recovered_record=[recovered]
#repeat for 1000 times:
#each susceptible individual has a beta*(the infected proportion) probability to become infected
#each infected individual has a gamma probability to become recovered
#record each population every time point in the arrays
for i in range(0,1000):
    susceptible_infected_list=list(np.random.choice(range(2),susceptible,p=[beta*infected/N,1-beta*infected/N]))
    infected_recovered_list=list(np.random.choice(range(2),infected,p=[gamma,1-gamma]))
    susceptible=susceptible_infected_list.count(1)
    infected=susceptible_infected_list.count(0)+infected_recovered_list.count(1)
    recovered=infected_recovered_list.count(0)+recovered
    #record
    susceptible_record.append(susceptible)
    infected_record.append(infected)
    recovered_record.append(recovered)
#plot the result
plt.figure(figsize=(6,4),dpi=150)
plt.plot(susceptible_record,label='susceptible')
plt.plot(infected_record,label='infected')
plt.plot(recovered_record,label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()
plt.show()