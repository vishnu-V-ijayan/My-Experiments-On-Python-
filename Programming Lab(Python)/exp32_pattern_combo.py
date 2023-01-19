#Program to print pattern using * No:03
count=int(input("Please enter the required number of rows  : "))
i=1
while(i<=count):
    j=1
    while(j<=i):
        print("*",end="")
        j=j+1
    print()
    i=i+1
i=count
while(i>=1):
    j=1
    while(j<i):
        print("*",end="")
        j=j+1
    print()
    i=i-1