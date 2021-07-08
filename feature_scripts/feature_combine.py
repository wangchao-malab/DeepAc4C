# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:40:49 2020

@author: Administer
"""

def feature_merge(feature_list,num_id,save_name):
    import numpy as np
    import pandas as pd
    n=0
    for fea in feature_list:
        # print(fea)
        n=n+1
        if n==1:           
            dfx=pd.read_csv(r'./features/mm/'+str(num_id)+'/f_b/'+str(fea),sep=',',header=0,index_col=0)
            # print((dfx.shape[1]))
        else:
            dfn=pd.read_csv(r'./features/mm/'+str(num_id)+'/f_b/'+str(fea),sep=',',header=0,index_col=0)
            dfx=pd.concat([dfx,dfn],axis=1)
        dfx1=pd.DataFrame(dfx) 
        dfx1.to_csv('./features/combined_features/'+str(save_name)+".csv",sep=",")
        
        
feature_list=['m_cksnap.csv', 'm_kmer.csv',  'm_SCPseDNC.csv','m_PseEIIP.csv',
                      'm_PseKNC.csv',  'm_SCPseTNC.csv','w2v_feature.csv']

def feature_combine():
    for num_id in [1,2,3,4,5,6,7,8,9,10]:
        feature_merge(feature_list,num_id,'feature_'+str(num_id))
