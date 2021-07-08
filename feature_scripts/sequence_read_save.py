# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:40:49 2020

@author: Administer
"""

def read_nucleotide_sequences(file):
    import re, os, sys
    if os.path.exists(file) == False:
        print(os.path)
        print('Error: file %s does not exist.' % file)
        sys.exit(1)
    with open(file) as f:
        records = f.read()
    if re.search('>', records) == None:
        print('Error: the input file %s seems not in FASTA format!' % file)
        sys.exit(1)
    records = records.split('>')[1:]
    fasta_sequences = []
    for fasta in records:
        array = fasta.split('\n')
        header, sequence = array[0].split()[0], re.sub('[^ACGTU-]', '-', ''.join(array[1:]).upper())
        sequence = re.sub('U', 'T', sequence)  #  replace U as T
        fasta_sequences.append([header, sequence])
    return fasta_sequences
 

def save_to_csv(encodings, file):
    with open(file, 'w') as f:
        for line in encodings[1:]:
            f.write(str(line[0]))
            for i in range(1,len(line)):
                f.write(',%s' % line[i])
            f.write('\n')

def file_remove():
    import os
    dir_list1=os.listdir("./features/")
    for x in dir_list1:
        if x.split(".")[-1]=="csv":
            os.remove("./features/"+str(x))
    for i in range(1,11,1):
        dir_list2=os.listdir("./features/mm/"+str(i))
        for x in dir_list2:
            if x.split(".")[-1]=="csv":
                os.remove("./features/mm/"+str(i)+"/"+str(x)) 
        dir_list3=os.listdir("./features/mm/"+str(i)+"/f_b/")
        for x in dir_list3:
            if x.split(".")[-1]=="csv":
                os.remove("./features/mm/"+str(i)+"/f_b/"+str(x))
                
    dir_list4=os.listdir("./features/combined_features/")
    for x in dir_list4:
        if x.split(".")[-1]=="csv":
            os.remove("./features/combined_features/"+str(x))
        
    # dir_list5=os.listdir("./results/")
    # for x in dir_list5:
        # os.remove("./results/"+str(x))