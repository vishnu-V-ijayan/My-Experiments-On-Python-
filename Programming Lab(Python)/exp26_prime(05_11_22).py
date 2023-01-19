#program to check whether the number is prime or not
num=int(input("enter a number  : "))
i=2
digit=0
while(i<num):
    if(num%i==0):
        digit=1
        print("the entered number is not a prime number...!")
    i=i+1
if(digit==0):
    print("the entered number is a prime number...!")

