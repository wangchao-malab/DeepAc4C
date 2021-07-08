# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:40:49 2020

@author: Administer
"""

import sys, os, re

def TriNcleotideComposition(sequence, base):
    trincleotides = [nn1 + nn2 + nn3 for nn1 in base for nn2 in base for nn3 in base]
    tnc_dict = {}
    for triN in trincleotides:
        tnc_dict[triN] = 0
    for i in range(len(sequence) - 2):
        tnc_dict[sequence[i:i + 3]] += 1
    for key in tnc_dict:
       tnc_dict[key] /= (len(sequence) - 2)
    return tnc_dict

def PseEIIP(fastas, **kw):
    for i in fastas:
        if re.search('[^ACGT-]', i[1]):
            print('Error: illegal character included in the fasta sequences, only the "ACGT-" are allowed by this PseEIIP scheme.')
            return 0

    base = 'ACGT'

    EIIP_dict = {
        'A': 0.1260,
        'C': 0.1340,
        'G': 0.0806,
        'T': 0.1335,
    }

    trincleotides = [nn1 + nn2 + nn3 for nn1 in base for nn2 in base for nn3 in base]
    EIIPxyz = {}
    for triN in trincleotides:
        EIIPxyz[triN] = EIIP_dict[triN[0]] + EIIP_dict[triN[1]] + EIIP_dict[triN[2]]

    encodings = []
    header = ['#'] + trincleotides
    encodings.append(header)

    for i in fastas:
        name, sequence = i[0], re.sub('-', '', i[1])
        code = [name]
        trincleotide_frequency = TriNcleotideComposition(sequence, base)
        code = code + [EIIPxyz[triN] * trincleotide_frequency[triN] for triN in trincleotides]
        encodings.append(code)
    return encodings

def PseEIIP_feature(fastas):   
    import sequence_read_save
    encodings = PseEIIP(fastas)
    sequence_read_save.save_to_csv(encodings, "./features/PseEIIP.csv")
    
if __name__ == '__main__':
    import os
    import sequence_read_save    
    os.chdir('C:/Users/Administer/Desktop/DeepAc4C-master/')
    fastas = sequence_read_save.read_nucleotide_sequences("./sequence/input.fasta")
    PseEIIP_feature(fastas)














