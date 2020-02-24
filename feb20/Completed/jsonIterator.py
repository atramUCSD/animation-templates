#Imports
import numpy as np
import pandas as pd
import json
import re
import pprint as pp
import io, os, sys, types, re


#initialize dataframe for all synsetRatings 
dfSynsets = pd.read_csv('synsetRating.csv') 

#Loaded in gentle generated JSON
with open('edited.json', 'r') as j:
     contents = json.loads(j.read())


'''
#Delete unnecessary values from words key in gentle generated JSON
with open('dest_file.json', 'w') as dest_file:
    with open('test1.json', 'r') as j:
        contents = json.loads(j.read())
        for value in contents['words']:
            del(value['case'])
            del(value['endOffset'])
            del(value['startOffset'])
            value.pop("phones",None)
        dest_file.write(json.dumps(contents,indent = 4))
'''

#Create function that appends JSON objects when the value:word == rows with word
def apply_fun (row):
    for value in contents['words']:
        if (value['word'] == row['word']):
            return json.dumps(value)

'''
# Print word equivalencies onto terminal. Checkpoint. 
row,col = dfSynsets.shape
for value in contents['words']:
    current_word = value['word']
    for csv_row in range(row):
        curr_csv_word = dfSynsets.loc[csv_row][-1]
        if curr_csv_word == current_word:
            print(curr_csv_word)
            print(current_word)
'''

# Use lambda row to apply function across all rows
x = dfSynsets.apply(lambda row : apply_fun(row),axis=1)
#Insert json data to new column
dfSynsets.insert(4,'json_ref',x)

# Output to excel file
dfSynsets.to_excel(r'newCSV.xlsx', index = None, header=True)
#Output to json file
dfSynsets.to_json(r'newJSON.json',indent = 4)
