### python script to read table into program to identify distance between MCO within a chromosome of and individual, and then calculate the distance between COs


import csv
import sys
#import argparse

file_name = sys.argv[1]
#out_file = sys.argv[2]

# path to file of interest, may want to use sys.argv[1] instead in order to add the filename and path on command input line instead of changing in file each time
#file_name = "/mnt/c/Users/Penny/Desktop/CO_V4_data/T_test_Midpt"
out_file = open("/mnt/c/Users/Penny/Desktop/CO_V4_data/out_file", "w+")

#create list of columns (list of lists) to use to contain data from column 3,4
columns = []
#create a list of columns with floats and string entries
columns2=[]



# step to read in csv file and assign to variable file_name
with open (file_name, 'r') as csvfile:
# read in each line of the file for each reported CO
        for line in csvfile.readlines()[0:]:
# will split each line at the tab between columns, file is a 5 columns - chromosmoe, start, stop, individual, midpt
                tmp = line.split('\t')
# for each column convert to a float or leave as a string (may need to change 
#this because first column is chromosome # which is not a float value.
                for entry in tmp:
                	try:
                		columns2.append(float(entry))
                	except ValueError:
                		columns2.append(entry)

#for each item in columns2 list of list assign column 4 "individual" and column 5
#"midpt average" to list of lists "columns"
for i in range(0,len(columns2),5):
	columns.append([columns2[i+3], columns2[i+4]])

#with open(out_file, 'w+') as csvfile:
#Working through list of lists "column" to find items of interest, aka data table
for x in range(0,len(columns)):
# x value is row, second [] is column location	
# if x value "individual" is a match to the x value "individual" in next row
	if (columns[x][0] == columns[x+1][0]):
		print(columns[x+1][1]-columns[x][1])
# find the distance (difference) between CO midpoints on a chromosome in the same individual
		distance = (columns[x+1][1]-columns[x][1])
		out_file.write(str(distance)+'\n')
#move one row in column 3
		x = x +1
		

out_file.close()


#out_file = open("/mnt/c/Users/Penny/Desktop/CO_V4_data/out_file")
#out_file.write(columns.append((tmp[3],tmp[4])))
#out_file.close()
	
#data = list(list(rec) for rec in csv.reader (csvfile, delimiter='\t'))


#previous code from Choichi using temporary variables
#read in each line of the file for each reported CO
#        for line in csvfile.readlines()[0:]:
#                print(line)
# will split each line at the tab between columns, file is a 5 columns - 
#chromosmoe, start, stop, individual, midpt
#                tmp = line.split('\t')
#                print(tmp)

#TRYING TO assign float values to list of values
#def traverse(o, tree_types=(list, tuple)):
#	if isinstance(o, tree_types):
#		for value in o:
#			for subvalue in traverse(value, tree_types):
#				yield subvalue
#	else:
#		yield o
#		
#def is_number(s):
#	try:
#		float(s)
#		return float(s)
#	except ValueError:
#		return s
