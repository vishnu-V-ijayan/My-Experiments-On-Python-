# Program to read file content and store it into a list using readlines().
open_file=open('file_01.txt','r')
File_Lines=open_file.readlines()

# Without using strip method
print("\nFile content with newline character  :  ")
print(File_Lines)

# Using strip method
print("\nFile content after removing newline character  :  ")
#File_Lines=[X.strip() for X in File_Lines]
#print(File_Lines)
print([X.strip() for X in File_Lines])  #==>using list comprehension,we can avoid the above steps
open_file.close()


