#find difference between 2 time parameters
#find sum of 2 time
class Time:
    def __init__(self,hour,minute,second):
        self.__hour=hour
        self.__minute=minute
        self.__second=second


    def __lt__(self,others):
        if(self.__hour>others.__hour):
            return ("True")
        elif(self.__hour==others.__hour):
            if(self.__minute < others.__minute):
             return ("True")
        elif(self.__minute == others.__minute):
            if (self.__second < others.__second):
                return ("True")
            else:
                return("False")
        else:
            return("False")

h=int(input("Enter the hour  : "))
m=int(input("Enter the minute  : "))
s=int(input("Enter the second  : "))
h1=int(input("Enter the hour  : "))
m1=int(input("Enter the minute  : "))
s1=int(input("Enter the second  : "))
t1=Time(h,m,s)
t2=Time(h1,m1,s1)

if(t1<t2):
    print(t2," is greater")
else:
    print(t1," is greater")

