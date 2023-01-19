#program to add 'ing' at the end of a given string if it already exists 'ing' then to add 'ly'.
x=str(input("Enter a String : "))

if(x[-3:]=="ing"):
    x=x+"ly"
else:
    x=x+"ing"
print(x)