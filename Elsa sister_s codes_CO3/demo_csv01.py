#Program to Read any csv file line by line
import csv
f=open("govtData.csv",newline='')
csv_reader=csv.reader(f)
print(next(csv_reader))
print(next(csv_reader))
print(next(csv_reader))