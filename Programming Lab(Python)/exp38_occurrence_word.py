#program to find the occurence of each word in a line of text

string=input("Enter the required content : ")
split=string.split(" ")
set=set(split)
for i in (set):
    occr=string.count(i)
    print(i,"occurs",occr,"times")