#import libraries
import os
import xml.dom.minidom
import xml.sax
import datetime
import matplotlib.pyplot as plt
#move to where the xml file is
os.chdir("C:/Users/24181/Desktop/IBI practical/IBI1_2023-24/Practical14")
#DOM
#start time
domstart=datetime.datetime.now()
#parse the XML file into a DOM document object
DOMTree=xml.dom.minidom.parse("go_obo.xml")
#get the root element
root=DOMTree.documentElement
#a list of terms elements
terms=root.getElementsByTagName('term')
#create three variables to store the number of three ontologies
molecular_function=0
biological_process=0
cellular_component=0
#take every term
for term in terms:
    #take the namespace element of this term
    namespace=term.getElementsByTagName('namespace')[0].firstChild.nodeValue
    #count the number
    if namespace=='molecular_function':
        molecular_function+=1
    if namespace=='biological_process':
        biological_process+=1
    if namespace=='cellular_component':
        cellular_component+=1
#print the result
print('DOM:')
print('molecular function: ',molecular_function)
print('biological process: ',biological_process)
print('cellular component: ',cellular_component)
#end time
domend=datetime.datetime.now()
#calculate and print the time
print('DOM time: ',domend-domstart)
#SAX

#draw the plot
ontology=['molecular function','biological process','cellular component']
number=[molecular_function,biological_process,cellular_component]
plt.bar(ontology,number,)
plt.title('number of ontologies(DOM)')
plt.xlabel('ontology')
plt.ylabel('number')
plt.show()
plt.clf()