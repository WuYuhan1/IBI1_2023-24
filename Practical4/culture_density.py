#repeat day+1 and cell*2 until cell>0.9
#display the number of day when cell>0.9
cell=0.05
day=1
while cell<=0.9:
    cell=cell*2
    day=day+1
print('On the '+str(day)+'th day, the cell density goes over 90%, which is the maximum number of days I can have a holiday from the lab. ')

