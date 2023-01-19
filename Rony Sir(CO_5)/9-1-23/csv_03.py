# Write a Python program to write a Python dictionary to a csv file.
# After writing the CSV file read the CSV file and display the content.

import csv

# Data to be inserted
data = [{'Name': 'John', 'Age': 25, 'Country': 'United States'},
{'Name': 'Mike', 'Age': 32, 'Country': 'Canada'},
{'Name': 'Sarah', 'Age': 35, 'Country': 'United Kingdom'}]

# Write to CSV file
with open('people.csv', 'w') as csvfile:
  headernames = ['Name', 'Age', 'Country']
  csvwriter = csv.DictWriter(csvfile, fieldnames=headernames)
  csvwriter.writeheader()
  for row in data:
     csvwriter.writerow(row)

# Read from CSV file and print contents
with open('people.csv', 'r') as csvfile:
 reader = csv.DictReader(csvfile)
 for row in reader:
   print(row)