#program to input a list of intigers and to remove even numbers from the same
limit=int(input("Enter the limit  :  "))
list=[]
for i in range(limit):
    element=int(input("Enter the elements  :  "))
list.append(element)
#print("List before sorting  : ",temp)
for i in list:
    if(i%2==0):
        list.remove(i)
print("list after removing  even numbers",list)
