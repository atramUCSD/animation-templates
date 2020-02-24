import numpy as np
import pandas as pd
import json
import re
import pprint as pp
import io, os, sys, types, re

#initialize dataframe for csv combination of gentle generated JSON and synsetRating csv
dfRefine = pd.read_excel('Finally.xlsx') 

#Drop rows without a gentle equivalent
dfRefine = dfRefine[dfRefine['json_ref'].notna()]

#Drop unnecessary column
dfRefine = dfRefine.drop(dfRefine.columns[-1],axis=1)

#Output to excel
dfRefine.to_excel(r'gentleMatches.xlsx', index = None, header=True)

#Output to json 
dfRefine.to_json (r'gentleMatches.json',indent = 4)