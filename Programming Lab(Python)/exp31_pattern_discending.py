#program to print pattern using *
count=int(input("Please enter the required number of rows  : "))
i=count+1
while(i>=1):
    j=1
    while(j<i):
        print("*",end="")
        j=j+1
    print()
    i=i-1