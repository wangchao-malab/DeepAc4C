#!/usr/bin/env python
#_*_coding:utf-8_*_

def kmerArray(sequence, k):
    kmer = []
    for i in range(len(sequence) - k + 1):
        kmer.append(sequence[i:i + k])
    return kmer


def Kmer(fastas, k=2, type="DNA", upto=False, normalize=True, **kw):
    import re
    import itertools
    from collections import Counter
    encoding = []
    header = ['#', 'label']
    NA = 'ACGT'
    if type in ("DNA", 'RNA'):
        NA = 'ACGT'
    else:
        NA = 'ACDEFGHIKLMNPQRSTVWY'

    if k < 1:
        print('Error: the k-mer value should larger than 0.')
        return 0

    if upto == True:
        for tmpK in range(1, k + 1):
            for kmer in itertools.product(NA, repeat=tmpK):
                header.append(''.join(kmer))
        encoding.append(header)
        for i in fastas:
            name, sequence, = i[0], re.sub('-', '', i[1])
            count = Counter()
            for tmpK in range(1, k + 1):
                kmers = kmerArray(sequence, tmpK)
                count.update(kmers)
                if normalize == True:
                    for key in count:
                        if len(key) == tmpK:
                            count[key] = count[key] / len(kmers)
            code = [name,]
            for j in range(2, len(header)):
                if header[j] in count:
                    code.append(count[header[j]])
                else:
                    code.append(0)
            encoding.append(code)
    else:
        for kmer in itertools.product(NA, repeat=k):
            header.append(''.join(kmer))
        encoding.append(header)
        for i in fastas:
            name, sequence = i[0], re.sub('-', '', i[1])
            kmers = kmerArray(sequence, k)
            count = Counter()
            count.update(kmers)
            if normalize == True:
                for key in count:
                    count[key] = count[key] / len(kmers)
            code = [name,]
            for j in range(2, len(header)):
                if header[j] in count:
                    code.append(count[header[j]])
                else:
                    code.append(0)
            encoding.append(code)
    return encoding


def kmer_feature(fastas):
    import sequence_read_save
    encodings = Kmer(fastas, 3, "DNA", True, False,)
    sequence_read_save.save_to_csv(encodings,"./features/kmer.csv")
    
if __name__ == '__main__':
    import os
    import sequence_read_save
    
    os.chdir('C:/Users/Administer/Desktop/DeepAc4C-master/')
    fastas = sequence_read_save.read_nucleotide_sequences("./sequence/input.fasta")
    kmer_features(fastas)
    
  