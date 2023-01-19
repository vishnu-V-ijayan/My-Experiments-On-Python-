# program to check whether the number is palindrome or not
num = int(input("enter a number  : "))
sum = 0
while (num != 0):
    digit = num % 10
    sum = sum + digit
    num = num // 10
print("the sum of digits of the number is  : ", sum)
