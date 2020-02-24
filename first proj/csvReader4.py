import pandas as pd 

import numpy as np

df = pd.read_excel('FinalTest.xlsx')

#df['score'] = df['score'].astype(int)

#df['score'] =  df['score'].apply(lambda x: x.replace('[','').replace(']','')) 
#df['mean'] =  df['mean'].apply(lambda x: x.replace('[','').replace(']','')) 
#df['std'] =  df['std'].apply(lambda x: x.replace('[','').replace(']','')) 

df['mean'] = df['mean'].astype(float)
df['std'] = df['std'].astype(float)
print(df)



#df = pd.read_excel('ChTest.xlsx')

#f2 = pd.read_excel('AlmostDone.xlsx')

#df = df.sort_values(by = ['video id'] , ascending = True)

#new_df = pd.merge(df, df2, how='inner', on=['video id'])

#df = df.drop_duplicates(subset='videoID', keep="first")

#print(df)
#print(df2)

#df = df.to_excel(r'C:\Users\alant\Desktop\ChTest.xlsx', index = None, header=True)

#print(new_df)

df = df.to_excel(r'C:\Users\alant\Desktop\FinalTest.xlsx', index = None, header=True)
