import pandas as pd 

import numpy as np

#number of participant votes per video id
#Calculate the mean of scores per unique video id 
#standard deviation
#then append channel names file 


# Load in file
df = pd.read_excel('Haijun Doc.xlsx' , names = ['video id' , 'score' , 'participant id'])
df2 = pd.read_excel('Haijun Doc.xlsx' , names = ['video id' , 'score' , 'participant id'])
df3 = pd.read_excel('mean.xlsx', names = ['score'])


records = df.to_dict(orient='records')

df2 = df2.groupby('video id')['participant id'].agg(['nunique']).reset_index()

for row in records:
    df = df.groupby('video id').agg(lambda x: x.values.tolist()).reset_index()
    break

df3['score'] = df.apply(lambda row: [[pd.np.std(row['score'])]], axis=1)

print(df3)
    

#print(df)
#print(df2)

#df = df.to_excel(r'C:\Users\alant\Desktop\test2.xlsx', index = None, header=True)
#df2 = df2.to_excel(r'C:\Users\alant\Desktop\test2.xlsx', index = None, header=True)
df3 = df3.to_excel(r'C:\Users\alant\Desktop\std.xlsx', index = None, header=True)