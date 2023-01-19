#program to print patterns
num=int(input("Enter the count  :  "))
i=1
while(i<=num):
    j=0
    while(j<i):
        print("*",end="")
        j=j+1
    print()
    i=i+1