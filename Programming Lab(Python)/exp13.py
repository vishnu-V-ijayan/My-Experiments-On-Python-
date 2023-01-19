# program to accept a file name from the user and print extension from that file
fileName = input("Enter a file name with extension  :  ")
print("fileName is", fileName)
m = fileName.split(".")
print("the extension of the above stated file is  : ", m[-1])
