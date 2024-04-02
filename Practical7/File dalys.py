#import python libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#change the working directory where the needed file is stored
os.chdir("C:/Users/24181/Desktop/IBI practical/IBI1_2023-24/Practical7")
#read the content of the file into a dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")
#show the data in specific rows and columns
print(
    dalys_data.iloc[0:101:10,3])#row1,11,...101, column4
#show the data with specific row name and column name
print(
    dalys_data.loc[
        (dalys_data.iloc[:,0]=="Afghanistan")#row Afghanistan
        ,"DALYs"])#column DALYs
#store data of China separately
china_data=dalys_data.loc[(dalys_data.iloc[:,0]=="China"),:]
#calculate the mean of DALYs in China
china_mean_dalys=np.mean(china_data.loc[:,"DALYs"])
print(china_mean_dalys)
#find DALYs in China in 2019
china_2019_dalys=np.mean(china_data.loc[(china_data.iloc[:,2]==2019),"DALYs"])
print(china_2019_dalys)
#compare the data
if china_2019_dalys < china_mean_dalys:
    print('The DALYs in China in 2019 was less than the mean.')
else:
    print('The DALYs in China in 2019 was greater than the mean.')
#plot the data for China
plt.plot(china_data.Year, china_data.DALYs, 'b+')
plt.title("DALYs in China")
plt.ylabel("DALYs")
plt.xlabel("Year")
plt.xticks(china_data.Year,rotation=-60)
plt.show()
plt.clf()
#Question:Are there places in the World where the DALYs in 2019 is less than 18,000? If so, where are they?
dalys_data_2019=dalys_data.loc[(dalys_data.iloc[:,2]==2019),:]#find data in 2019
low_dalys_places=dalys_data_2019.loc[(dalys_data_2019.iloc[:,3]<18000),:]#find data in 2019 which DALYs<18000
print('Yes. They are')
print(low_dalys_places.iloc[:,0])#show the names of the countries