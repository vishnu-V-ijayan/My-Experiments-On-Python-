#Program to generate a simple calculator

num1=int(input("Enter the first number  "))
num2=int(input("Enter the second number  "))

op=int(input("Enter the operation. 1=sum, 2=difference,3=quotient, 4=product  "))
if(op==1):
    print("the result is  ", num1+num2)
elif (op==2):
    print("the result is  ", num1-num2)
elif (op==3):
    print("the result is  ", num1*num2)
elif (op==4):
    print("the result is  ", num1/num2)
else:
    print("invalid operator")

