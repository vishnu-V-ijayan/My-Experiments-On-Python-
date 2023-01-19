# program to check whether the number is palindrome or not
num = int(input("enter a number  : "))
temp = num
rev = 0
while (temp > 0):
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10
print("the reverse of the number is  : ", rev)
if (num == rev):
    print("above listed number is a palindrome...!")
else:
     print("above listed number is not palindrome...!")
