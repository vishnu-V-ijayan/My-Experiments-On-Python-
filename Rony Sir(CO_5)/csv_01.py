#Read and print each row rom a csv file(As list)
import csv

# Open csv file
with open('csv_file.csv','r') as file:
    # Create a csv reader
    reader= csv.reader(file)
    # Iterate over the rows of the csv file
    for row in reader:
        # Print the row as a list of strings
        print(row)
