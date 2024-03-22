#import module
import matplotlib.pyplot as plt
#create variables showing the time of the activities
sleeping=8
classes=6
studying=3.5
tv=2
music=1
other=24-sleeping-classes-studying-tv-music
#create a dictionary whose keys are activities and values are the time(the variables created in step1)
activity_time={'Sleeping':sleeping,
               'Classes':classes,
               'Studying':studying,
               'TV':tv,
               'Music':music,
               'Other':other}
#print the dictionary
print(activity_time)
#make the pie chart which matches the datas in the dictionary
activity=["Sleeping", "Classes", "Studying", "TV", "Music", "Other"]
time=[activity_time['Sleeping'],
      activity_time['Classes'],
      activity_time['Studying'],
      activity_time['TV'],
      activity_time['Music'],
      activity_time['Other']]
plt.figure()
plt.pie(time,labels=activity,startangle=90)
plt.show()
plt.clf()
