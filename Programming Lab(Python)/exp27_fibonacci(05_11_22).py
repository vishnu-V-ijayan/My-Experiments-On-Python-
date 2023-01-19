# program to print fibonacci series
num = int(input("enter a number  : "))
a = 0
b = 1
i = 2
print("fibonacci series   :")
while (i <= num):
    print(b)
    a, b = b, (a + b)
    i += 1
