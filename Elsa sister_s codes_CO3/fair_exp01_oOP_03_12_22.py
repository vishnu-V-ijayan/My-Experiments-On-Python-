#program to find the area,perimeter of the rectangle1 & rectangle2 using object oriented programming and compare them
class Rectangle():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length + self.breadth)
l1=float(input("Enter the length of first rectangle  :  "))
b1=float(input("Enter the width of first rectangle  :  "))
l2=float(input("Enter the length of second rectangle  :  "))
b2=float(input("Enter the width of second rectangle  :  "))
rect1=Rectangle(l1,b1)
rect2=Rectangle(l2,b2)
print("Area of the first rectangle is {} and perimeter is {} : ".format(rect1.area(),rect1.perimeter()))
print("Area of the second rectangle is {} and perimeter is {} : ".format(rect2.area(),rect2.perimeter()))
print(rect1.area()>rect2.area())
print(rect1.perimeter()>rect2.perimeter())