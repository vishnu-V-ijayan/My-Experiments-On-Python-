#program to check whether the given number is armstrong or not
num=int(input("enter a number  : "))
temp=num
armstrong=0
while(temp!=0):
    digit=temp%10
    armstrong=armstrong+(digit*digit*digit)
    temp=temp//10
if(armstrong==num):
    print("the given number is armstrong...!")
else:
    print("the given number is not armstrong...!")