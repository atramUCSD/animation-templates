import json
import pprint
from operator import attrgetter
import pandas as pd

#Load in json file as data

f = open('connectionRating.json')
conns = json.load(f)['connections']
sortedRatings = sorted(filter(lambda x: x["rating"] <= 1, conns), key=lambda x: x["rating"])

# check typings 
print(type(sortedRatings[0]))
print(type(sortedRatings))


#delete examples values in json
for rating in sortedRatings:
    if 'examples' in rating:
        del rating['examples']


#outputs list to json formatting 

with open('result.json', 'w') as fp:
  fp = json.dump(sortedRatings, fp, indent=4)
