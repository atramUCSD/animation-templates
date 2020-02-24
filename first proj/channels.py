import pandas as pd

df = pd.read_csv('4cbfc50b694243df91862a8dab13f5bd.csv')


df = df.drop(['|__videoId'], axis = 'columns') 

print(df[0:10])
#df.to_csv('channels.csv')