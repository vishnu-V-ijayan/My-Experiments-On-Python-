#program to generate list of positive numbers from list of integers
myList=[]
myList1=[]
myList2=[]
size=int(input("Enter the size of the list : "))
for i in range(size):
    elements=int(input("Enter any integers to be added to the list : "))
    myList.append(elements)
print("The entered list is : ",myList)
myList1=[i for i in myList if i>0]
myList2=[i for i in myList if i<0]
print("The list of positive numbers are  :  ", myList1)
print("The elements removed from the list are  :  ", myList2)
