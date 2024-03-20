#input population of cities
#make the list
#print the list
Edinburgh=0.56
Glasgow=0.62
Stirling=0.04
London=9.7
Haining=0.58
Hangzhou=8.4
Shanghai=29.9
Beijing=22.2 
uk_city_population=[Edinburgh,Glasgow,Stirling,London]
china_city_population=[Haining,Hangzhou,Shanghai,Beijing]
print(uk_city_population)
print(china_city_population)
#make bar plots
import matplotlib.pyplot as plt
#cities of UK
plt.ylabel("Population(millions)")
plt.title("City size in the UK")
uk_city_name=["Edinburgh","Glasgow","Stirling","London"]
plt.bar(range(len(uk_city_population)),uk_city_population,tick_label=uk_city_name)
plt.show()
plt.clf()
#cities of China
plt.ylabel("Population(millions)")
plt.title("City size in China")
china_city_name=["Haining","Hangzhou","Shanghai","Beijing"]
plt.bar(range(len(china_city_population)),china_city_population,tick_label=china_city_name)
plt.show()
plt.clf()