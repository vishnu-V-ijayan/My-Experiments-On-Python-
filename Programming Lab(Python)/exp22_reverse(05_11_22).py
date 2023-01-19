# program to find the reverse of a number
number = int(input("enter the number  : "))
rev=0
while (number > 0):
    digit = number % 10
    rev=rev*10+digit
    number = number // 10
print("the reverse of the given number is : ", rev)
