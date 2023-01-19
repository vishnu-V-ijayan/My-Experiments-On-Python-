#program to print leap years within the specified range
limit=int(input("Please enter the range  :  "))
print("The leap years are  :  ")
for i in range(2022,limit+1):
    if i%4==0:
        print(i)