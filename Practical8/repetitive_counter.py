seq='ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'#input the sequence being counted
seq_test=' '+seq+' '#add two space at both ends of the sequence to count in order to count the repeat instances at the ends
gtgtgt=seq.split('GTGTGT')
gtctgt=seq.split('GTCTGT')#split the sequence at the repeat sequence
repeat_number=len(gtgtgt)-1+len(gtctgt)-1#the number of parts after being splited = number of repeat elements + 1
print(repeat_number)