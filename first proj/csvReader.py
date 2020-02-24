
#Don't open csv, and directly run it 

#Read the entire csv file line by line, gather video id's per line as a key 
# The values will be all the responses. 
# Use dictionary to sort responses. 
# Loop through key and value pairs.
# For each video calculate all the responses within the array, implement average and standard deviation functions. 


# *Priority* 
#Video ID, the amount of responses for that id, the average scores, and standard deviation of scores, channel name 

#For JSON value, use video id within the channels file as a key as well
#Use the channel name as the value. 

# importing csv module 
import csv 

# csv file name 
filename = "video_responses.csv"

# initializing the titles and rows list 
fields = [] 
rows = [] 

# reading csv file 
with open(filename, 'r') as csvfile: 
	# creating a csv reader object 
	csvreader = csv.reader(csvfile) 
	
	# extracting field names through first row 
	fields = next(csvreader)

	# extracting each data row one by one 
	for row in csvreader: 
		rows.append(row) 

	# get total number of rows 
	print("Total no. of rows: %d"%(csvreader.line_num)) 

# printing the field names 
print('Field names are:' + ', '.join(field for field in fields)) 


# printing first 5 rows 
#print('\nFirst 5 rows are:\n') 
#for row in rows[:5]: 
#	# parsing each column of a row 
#	for col in row: 
#		print("%20s"%col), 
#	print('\n') 

# sorting rows based on fields 
with open(filename, 'r', newline='') as f_input:
    csv_input = csv.DictReader(f_input)
    data = sorted(csv_input, key=lambda row: (row['score'], row['familiarity of infographic videos']))

with open('output2.csv', 'w', newline='') as f_output:    
    csv_output = csv.DictWriter(f_output, fieldnames=csv_input.fieldnames)
    csv_output.writeheader()
    csv_output.writerows(data)
