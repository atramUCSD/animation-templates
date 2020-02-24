import json
import pprint
import pandas as pd

df = pd.read_csv('filteredSynset.csv') 

# strip words of brackets
#df['words'] = df['words'].str.strip('[]')

#inherent function in pandas, but oddly doesn't work
#df = df.explode('words')


#df = df.set_index(['synset','rating']).apply(pd.Series.explode) # this would work for exploding multiple columns as well

# then reset the index

#df = df.reset_index()

'''
#attempt at listing words column
for item in df['words']:
    item = list(item)
'''

#Not a list checker
for i in df['words'] :
    if(not isinstance(i,list)):
        print(type(i))


#df = df.to_excel(r'C:\Users\alant\Desktop\test.xlsx', index = None, header=True)