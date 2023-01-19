#program to show appropriate prompt message
li=[]
n=int(input("Enter the limit  :  "))
for i in range(n):
    el=int(input("Enter the number  :  "))
    if el>100:
        el="over"
    li.append(el)
print(li)

