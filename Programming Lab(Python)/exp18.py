# program to create single string seperated with spaces from two strings by swapping the character at position one
w1 = "my"
w2 = "fate"
singleString = w1 + " " + w2
print("singleString", singleString)
a = w1[0]
b = w2[0]
c = w1[1:]
d = w2[1:]
newString = b + c + " " + a + d
print("the new string after swapping is  :  ", newString)
