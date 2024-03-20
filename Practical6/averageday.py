#create variables showing the time of the activities
#create a dictionary whose keys are activities and values are the time(the variables created in step1)
#print the dictionary
sleeping=8
classes=6
studying=3.5
tv=2
music=1
other=24-sleeping-classes-studying-tv-music
activity_time={'Sleeping':sleeping,
               'Classes':classes,
               'Studying':studying,
               'TV':tv,
               'Music':music,
               'Other':other}
print(activity_time)
#make the pie chart matches the datas in the dictionary
import matplotlib.pyplot as plt
activity=["Sleeping", "Classes", "Studying", "TV", "Music", "Other"]
time=[activity_time['Sleeping'],activity_time['Classes'],activity_time['Studying'],activity_time['TV'],activity_time['Music'],activity_time['Other']]
plt.figure()
plt.pie(time,labels=activity,startangle=90)
plt.show()
plt.clf()