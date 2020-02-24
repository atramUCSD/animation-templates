import json
import pprint
from operator import attrgetter

#Load in json file as data
f = open('connectionRating.json')
data = json.load(f)
f.close()

'''

#convert dictionary to list
jsonList = [[piece['synset'], piece['rating'], piece['words']] for piece in data['connections']]

#Type checker
Type = type(jsonList)

#print first item in list 
length = len(jsonList)
print(length)

'''

'''
for item in :
    print(item["rating"])
'''
f = open('connectionRating.json')
conns = json.load(f)['connections']
sortedRatings = sorted(filter(lambda x: x["rating"] <= 1, conns), key=lambda x: x["rating"])

print(type(sortedRatings[0]))
print(type(sortedRatings))
#sorted_by_rating = [x for x in sorted_by_rating if sorted_by_rating != 20]


#print(sorted_by_rating)

for rating in sortedRatings:
    if 'examples' in rating:
        del rating['examples']

df = df.set_index(['synset','rating']).apply(pd.Series.explode) # this would work for exploding multiple columns as well

# then reset the index

df = df.reset_index()

#outputs list to json formatting 

with open('result.json', 'w') as fp:
  fp = json.dump(sortedRatings, fp, indent=4)

df = df.to_csv(r'test2.csv', index = None, header=True)
