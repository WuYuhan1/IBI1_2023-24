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
    elif namespace=='biological_process':
        biological_process+=1
    elif namespace=='cellular_component':
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
saxstart=datetime.datetime.now()
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
class gohandler(xml.sax.ContentHandler):
    def __init__(self):
        self.currentdata=''
        self.molecular_function=0
        self.biological_process=0
        self.cellular_component=0
        self.namespace=''
        self.a=0
    def startElement(self,tag,attributes):
        self.currentdata=tag
    def characters(self, content):
        if self.currentdata=='namespace':  
            self.namespace=content     
    def endElement(self,tag):
        if self.currentdata=='namespace':
            if self.namespace=='molecular_function':
                self.molecular_function+=1
            elif self.namespace=='biological_process':
                self.biological_process+=1
            elif self.namespace=='cellular_component':
                self.cellular_component+=1
        self.currentdata=''
    def printresult(self):
        print('molecular function: ',self.molecular_function)
        print('biological process: ',self.biological_process)
        print('cellular component: ',self.cellular_component)
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
handler=gohandler()
parser.setContentHandler(handler)
parser.parse('go_obo.xml')
print('SAX:')
handler.printresult()
saxend=datetime.datetime.now()
print('SAX time: ',saxend-saxstart)
#draw the plot
ontology1=['molecular function','biological process','cellular component']
number1=[molecular_function,biological_process,cellular_component]
plt.bar(ontology1,number1,)
plt.title('number of ontologies(DOM)')
plt.xlabel('ontology')
plt.ylabel('number')
plt.show()
plt.clf()

#compare the time
if domend-domstart>saxend-saxstart:
    print('DOM is quicker.')
if domend-domstart<saxend-saxstart:
    print('SAX is quicker.')
