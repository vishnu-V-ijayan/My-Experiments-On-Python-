# program to find the sum of even numbers within the range specified
n = int(input("enter the range   :  "))
i = 1
sum = 0
while (i <= n):
    if (i % 2 == 0):
        sum = sum + i
    i = i + 1
print(("sum of even numbers within "), (n), (" is : "), (sum))
