import numpy as np
import pandas as pd
import json
import re
import pprint
import io, os, sys, types, re
from pathlib import Path
import fileinput # implements a helper class and functions to loop over standard input or a list of files.
from glob import glob #finds all the pathnames matching a specified pattern
import jsondiff as jsondiff

#initialize dataframe for all subtitles
dfSubtitles = pd.read_csv('videoSubtitle.csv') 
#initialize dataframe for the universe transcript 
dfJson = pd.read_json('test1.json')

#Create properly formatted string in order to compare with csv file 
pd.set_option('display.max_colwidth', None)

#Retrieve only 1 iteration of the transcript
dfJsonTranscript = dfJson.get('transcript').to_string(index=False).strip()
dfJsonTranscript, sep, tail = dfJsonTranscript.partition('\n')

#create text file
text_file = open("sample.txt", "wt")
n = text_file.write(dfJsonTranscript)
text_file.close()

#initialize that text file as a string
with open('sample.txt', 'r') as file:
    data = file.read().replace('\n', '')

# the row where the string is located
Test = (dfSubtitles[dfSubtitles['subtitle'].str.contains(data, regex=False)]) 

Test = Test2.to_json(r'newJson.json', orient = 'records')