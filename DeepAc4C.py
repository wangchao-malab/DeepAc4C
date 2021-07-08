# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:40:49 2020

@author: Administer
"""

def DeepAc4C(input_file,output_file):
    import os,sys
    sys.path.append('./feature_scripts/')

    import Kmer,CKSNAP,PseEIIP,PseFeature
    import sequence_read_save
    import max_min_sele
    import w2v_kmer_corpus_feature, feature_combine,predict
    
    print("step_1: sequence checking......")
    fasta_dir=input_file
    fastas = sequence_read_save.read_nucleotide_sequences(fasta_dir)
    seq_id=[x[0] for x in fastas]
    
    print("step_2: sequence encoding......")
    Kmer.kmer_feature(fastas)
    CKSNAP.cksnap_feature(fastas)
    PseEIIP.PseEIIP_feature(fastas)
    PseFeature.Pse_feature(fastas)
    
    print("step_3: feature scale and selection......")
    max_min_sele.max_min()
    max_min_sele.feature_sele()
    w2v_kmer_corpus_feature.w2v_kmer_corpus()
    w2v_kmer_corpus_feature.w2v_features()
    feature_combine.feature_combine()
    predict.result_prediction(seq_id,output_file)
    sequence_read_save.file_remove()
    
if __name__=='__main__':
    import argparse
    import pandas as pd
    import os
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--inputfile", help="input fasta file",)
    parser.add_argument("-o","--outputfile", help="input fasta file",)
    args = parser.parse_args()
    input_file=args.inputfile
    output_file=args.outputfile
    print("work launched")
    DeepAc4C(input_file,output_file)
    print("job finished !")