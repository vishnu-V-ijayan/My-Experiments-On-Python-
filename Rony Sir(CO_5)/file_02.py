#Program to odd lines of file to another.
#Opening files for reading and writing.

input_file=open('File_01.txt','r')
output_file=open('File_02.txt','w')

#Coping/Reading contents from read_File to copy_data
copy_data=input_file.readlines()
print("Actual file content is  : ")
print(copy_data,"\n")

for i in range(0, len(copy_data)):
    if i%2==0:
        output_file.write(copy_data[i])
    else:
        pass

#Closing file after writing
output_file.close()

#Opening write file in read mode and printing values

output_file=open('File_02.txt','r')
print("Odd lines are  :  ")
print(output_file.read())

#Closing_files
input_file.close()
output_file.close()

