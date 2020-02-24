import pandas as pd
import re




#number of participant votes per video id
#Calculate the mean of scores per unique video id 
#standard deviation
#then append channel names file 




# Load in file
df = pd.read_excel('Haijun Doc.xlsx')

# Drop unnecessary columns
#df = df.drop(['duration for the task','participant age','familiarity of youtube videos','familiarity of infographic videos'], axis = 'columns')

#df = df.loc[~df['video id'].str.contains('#NAME?')]

# sort file by 0-3 score, and alphabetical id
df = df.sort_values(by = ['score','video id'] , ascending = True)

# calculate mean of score
#mean = df['score'].mean()


video_ids = df['video id']

scores = df['score']

participants = df['participants']

df = pd.DataFrame({'video id': video_ids,
               'score': scores, 'particpant id' : participants})

for i in df:

    new = df.groupby('video id')[participants].count()[i]

print(new)

# new column
#new_column = df['participant id'] + 1

#calculate the amount of participants per video id

#unique_value = df["video id"].nunique()
#print(unique_value)

# this line creates a new column, which is a Pandas series.
#new_column = df['participant id'] + 1
# we then add the series to the dataframe, which holds our parsed CSV file
#df['Votes per video id'] = new_column

#df['Votes per video id']=df.groupby(['video id']).cumcount().add(1).astype(str)

#print(df)


#print(df[0:10])

#df.to_excel(r'C:\Users\alant\Desktop\export_dataframe.xlsx', index = None, header=True)

#df.to_csv('new.txt', index=False, sep='\t')
