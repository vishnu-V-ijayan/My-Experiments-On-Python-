num=int(input("Enter the limit  :  "))
li=[]
for i in range(num):
    a=int(input("Enter the element  :  "))

    li.append(a)

newli=[i*i for i in li if i>0]
print("The squares are  :  ",newli)


