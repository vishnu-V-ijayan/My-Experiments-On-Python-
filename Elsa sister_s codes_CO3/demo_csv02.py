#Program to Read any csv file to its maximum
import csv
reader = csv.reader(open("govtData.csv"))
for row in reader:
    print(row)