#program to input a list of intigers and to remove odd numbers from the same

limit=int(input("Enter the limit  :  "))
list=[]
i=0
for i in range(limit):
    element=int(input("Enter the elements  :  "))
    if (i % 2 != 0):
        list.append(element)
print("list after removing  even numbers", list)