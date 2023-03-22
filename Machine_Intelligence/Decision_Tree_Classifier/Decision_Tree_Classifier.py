'''
Assume df is a pandas dataframe object of the dataset given
'''

import numpy as np
import pandas as pd
import random


'''Calculate the entropy of the enitre dataset'''
# input:pandas_dataframe
# output:int/float
def get_entropy_of_dataset(df):
    # TODO
    
    #print(df)
    #print(df.shape)
    t=tuple(df['play'])
    val=[]
    for i in t:
        val.append(i)
    #print(val)
        
    count_yes=0
    count_total=0
    count_no=0
    for i in val:
        count_total+=1
        #print(i)
        if i=='yes':
            count_yes+=1
        else:
            count_no+=1
    #print(count_total,count_yes,count_no)

    r1= (count_yes / count_total)
    v1= -r1 * np.log2(r1)
    r2= (count_no / count_total)
    v2= -r2 * np.log2(r2)

    result=v1+v2 
    #print(result)
    entropy=result
    
    return entropy


'''Return avg_info of the attribute provided as parameter'''
# input:pandas_dataframe,str   {i.e the column name ,ex: Temperature in the Play tennis dataset}
# output:int/float
def get_avg_info_of_attribute(df, attribute):
    # TODO

    t=tuple(df[attribute])
    val=[]
    for i in t:
        val.append(i)
    #print(val)

    x=df.groupby(attribute)
    y=dict()
    k=[]
    total=0
    for key,value in x:
        #print(key)
        k.append(key)
        l=list(value['play'])
        grp_count_no=0
        grp_count_yes=0
        grp_count_total=0
        for i in l:
            total+=1
            grp_count_total+=1
            if i=='yes':
                grp_count_yes+=1
            else:
                grp_count_no+=1
        y[key]={'yes':grp_count_yes, 'no': grp_count_no, 'total': grp_count_total}

    result=0
    for j in k:
        r1=y[j]['yes']/y[j]['total']
        r2=y[j]['no']/y[j]['total']
        if r1==0.0:
            v1=0.0
        else:
            v1= - r1 * np.log2(r1)
        if r2==0.0:
            v2=0.0
        else:
            v2= - r2 * np.log2(r2)
        r=v1+v2
        res= y[j]['total']/total * r
        result+=res
    
    #print(result)
    avg_info=result
    return avg_info


'''Return Information Gain of the attribute provided as parameter'''
# input:pandas_dataframe,str
# output:int/float
def get_information_gain(df, attribute):
    # TODO
    
    entropy = get_entropy_of_dataset(df)
    avg_attribute = get_avg_info_of_attribute(df, attribute)
    IG = entropy - avg_attribute
    return IG


#input: pandas_dataframe
#output: ({dict},'str')
def get_selected_attribute(df):
    '''
    Return a tuple with the first element as a dictionary which has IG of all columns 
    and the second element as a string with the name of the column selected

    example : ({'A':0.123,'B':0.768,'C':1.23} , 'C')
    '''
    # TODO

    IG=dict()
    for i in df.columns:
        if i != 'play':
            info_gain=get_information_gain(df, i)
            IG[i]=info_gain
            
    for j in IG:
        if IG[j] == max(IG.values()) :
            val=j

    t=(IG,val)
    #print(t)
    return t
    
