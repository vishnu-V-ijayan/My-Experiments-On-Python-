# program to check whether the entered number is positive,negative or zero
value = int(input("Enter a number  :  "))
if (value < 0):
    print("Entered number is a negative integer.")
elif (value == 0):
    print("Entered number is zero.")
else:
    print("Entered number is a positive integer.")
