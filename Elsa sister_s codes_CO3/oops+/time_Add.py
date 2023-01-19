# find sum of 2 time
class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        #t3 = Time()
        t3.__hour = t1.__hour + t2.__hour
        t3.__minute = t1.__minute + t2.__minute
        t3.__second = t1.__second + t2.__second
        if t3.__second > 59:
            t3.__second -= 60
            t3.minute = t3.__minute + 1
        if t3.__minute > 59:
            t3.__minute -= 60
            t3.__hour = t3.__hour + 1
        return (str(t3.__hour)+":"+str(t3.__minute)+":"+str(t3.__second))


h = int(input("Enter the hour  : "))
m = int(input("Enter the minute  : "))
s = int(input("Enter the second  : "))
h1 = int(input("Enter the hour  : "))
m1 = int(input("Enter the minute  : "))
s1 = int(input("Enter the second  : "))


def __lt__(self, others):
    if (self.__hour < others.__hour):
        return ("True")
    elif (self.__hour == others.__hour):
        if (self.__minute < others.__minute):
            return ("True")
    elif (self.__minute == others.__minute):
        if (self.__second < others.__second):
            return ("True")
        else:
            return ("False")
    else:
        return ("False")
t1 = Time(h, m, s)
t2 = Time(h1, m1, s1)
t3 = Time(0,0,0)
#print(t3)
print(t1+t2)
