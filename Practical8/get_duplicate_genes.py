#import libraries
import os
import re
os.chdir("C:/Users/24181/Desktop/IBI practical/IBI1_2023-24/Practical8")#move to where the fa file is
origin_file=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa')
genome=origin_file.read()#change the document into a string
duplication=re.findall(r'>.*?duplication.*?>',genome,re.S)
    #find the identify sequences whose description contains the word ‘duplication’
print(len(duplication))