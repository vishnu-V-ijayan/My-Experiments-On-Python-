#program to find the area of the rectangle using object oriented programming
class Rectangle():
    def __init__(self,l,w):
        self.length=l
        self.width=w
    def rectangle_area(self):
        return self.length*self.width

newRectangle=Rectangle(12,10)
print("The area of the rectangle is  :  :",newRectangle.rectangle_area())