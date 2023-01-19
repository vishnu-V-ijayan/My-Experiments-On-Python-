#program to find the area,perimeter of the rectangle1 & rectangle2 using object oriented programming and compare them
class Bank_Account:
    def __init__(self):
        self.balance=0
        print("Hello!!! Welcome to the deposit & withdrawal machine")
    def deposit(self):
        amount=float(input("Enter amount to be deposited  :  "))
        self.balance+=amount
        print("\n Amount Deposited  : ",amount)
    def withdraw(self):
        amount=float(input("Enter amount to be withdrawn  : "))
        if self.balance>=amount:
            self.balance-=amount
            print("You withdrew  : ",amount)
        else:
            print("\n Insufficient balance")
    def display(self):
        print("\n Net available balance  :  ",self.balance)
#Driver code
#Creating an object of class
s=Bank_Account()
#Calling functions with that class object
s.deposit()
s.withdraw()
s.display()

