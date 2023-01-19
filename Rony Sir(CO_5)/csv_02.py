#Read and print each row rom a csv file(As list) with specifying the columns
import csv

# Specify the column indices that you want to read
# e.g. column 0 is the first column, column 1 is the second column,etc.

columns_to_read=[0,2]

# Open csv file
with open('csvFile.csv','r') as file:
    # Create a csv reader
    clmn_reader= csv.reader(file)
    # Iterate over the rows of the csv file
    for row in clmn_reader:
        # print the contents of the specified columns
        print([row[i] for i in columns_to_read])

