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
sequence1=re.findall(r']([^>]*)',str(duplication),re.S)
#remove the \n
sequence=[]
for i in range(len(sequence1)):
    single_sequence=re.sub(r'\\n','',sequence1[i])
    sequence.append(single_sequence)
#input the sequence
repeat=input("'GTGTGT' or 'GTCTGT': ")
#find the required sequence 
#store information as stings in lists
repeat_number=[]
final_name=[]
final_sequence=[]
for i in range(len(sequence)):
    if re.search(repeat,sequence[i]):
        final_sequence.append(sequence[i])#gene sequence
        final_name.append(name[i])#gene name
        repeat_number.append(len((''+sequence[i]+'').split(repeat))-1)#the the	number of instances of the given repetitive element
#the function to write the file
def newfile():
    for i in range(len(final_sequence)):
        new_file.write(final_name[i]+' '+str(repeat_number[i]))
        new_file.write('\n')
        new_file.write(final_sequence[i])
        new_file.write('\n')
    return()
#decide the file name and create the file
if repeat=='GTGTGT':
    new_file=open('GTGTGT_duplicate_genes.fa','w')
    newfile()
elif repeat=='GTCTGT':
    new_file=open('GTCTGT_duplicate_genes.fa','w')
    newfile()
else:
    print("It's not one of the given sequence.")

