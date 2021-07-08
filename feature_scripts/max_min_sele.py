# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 22:40:49 2020

@author: Administer
"""

import os
import pandas as pd
from sklearn import preprocessing
import numpy as np
import math
# scale
def max_min():
    feature_dict={'cksnap_2':'cksnap', 'kmer_upto_3':'kmer',  'scpsednc_5':'SCPseDNC',
                  'PseEIIP':'PseEIIP', 'pseknc_k3_10':'PseKNC',  'scpsetnc_4':'SCPseTNC',}

    max_min_scale=pd.read_csv("./model/phyche_feature_minmax_scale.csv",index_col=0)
    if os.path.exists('./features/mm/')==False:
        os.mkdir('./features/mm/')
    if os.path.exists('./features/combined_features/')==False:
        os.mkdir('./features/combined_features/')
    for tn in [1,2,3,4,5,6,7,8,9,10]:
        if os.path.exists('./features/mm/'+str(tn))==False:
            os.mkdir('./features/mm/'+str(tn))
        dir_list=os.listdir()
        # print("working dir: ", os.getcwd()) 
        for x in ['cksnap.csv','kmer.csv','PseEIIP.csv','PseKNC.csv','SCPseDNC.csv','SCPseTNC.csv']:
            # print(x)
            xx=x.split(".")[0]
            dfx=pd.read_csv('./features/'+str(x),sep=',',header=None,index_col=None).iloc[:,1:]
            dfx_col=dfx.columns
            max_val=max_min_scale.loc[xx+'_max_'+str(tn)].to_numpy()
            max_val=np.array([x for x in max_val if not math.isnan(x)])
            min_val=max_min_scale.loc[xx+'_min_'+str(tn)].to_numpy()
            min_val=np.array([x for x in min_val if not math.isnan(x)])
            dfx_scale=(dfx.to_numpy()-min_val)/(max_val-min_val)
            pd.DataFrame(dfx_scale,columns=dfx_col).to_csv("./features/mm/"+str(tn)+"/m_"+str(xx)+".csv")

# 2 extract sele features
def feature_sele():
    sele_feature_id=pd.read_csv("./model/phyche_sele_feature.csv",index_col=0)
    for tn in [1,2,3,4,5,6,7,8,9,10]:
        if os.path.exists('./features/mm/'+str(tn)+"/f_b")==False:
            os.mkdir('./features/mm/'+str(tn)+"/f_b")
        dir_list=os.listdir()
        # print("working dir: ", os.getcwd()) 
        for x in ['m_cksnap.csv','m_kmer.csv','m_PseEIIP.csv','m_PseKNC.csv','m_SCPseDNC.csv','m_SCPseTNC.csv']:
            # print(x)
            xx=x.split(".")[0]
            
            dfx=pd.read_csv('./features/mm/'+str(tn)+"/"+str(x),sep=',',index_col=0)
            sele_feature=sele_feature_id.loc[xx.split("m_")[-1]+'_sele_'+str(tn)].to_numpy()
            sele_feature=np.array([str(int(x)) for x in sele_feature if not math.isnan(x)])

            dfx_sele=dfx[np.array(sele_feature)]
            pd.DataFrame(dfx_sele).to_csv("./features/mm/"+str(tn)+"/"+"f_b/"+str(xx)+".csv")