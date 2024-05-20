#import libraries
import os
import re
os.chdir("C:/Users/24181/Desktop/IBI practical/IBI1_2023-24/Practical8")#move to where the fa file is
origin_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
genome=origin_file.read()#change the document into a string
#find the identify sequences whose description contains the word ‘duplication’
duplication=re.findall('>[^\n]*?duplication[^>]*',genome,re.S)
#simplify
name=re.findall(r'>[^ ]*',str(duplication),re.S)
sequence=re.findall(r']([^>]*)',str(duplication),re.S)
#create the new file
new_file=open('duplicate_genes.fa','w')
for i in range(len(sequence)):
    new_file.write(name[i])
    new_file.write('\n')#linefeed
    sequence1=re.sub(r'\\n','',sequence[i])#remove the \n in the string
    new_file.write(sequence1)
    new_file.write('\n')#linefeed
new_file.close()
