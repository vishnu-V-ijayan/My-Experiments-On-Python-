# program to create a list of colors from comma seperated color names entered by the user
# display first and last color
color = []
print("Enter different colors  :  ")
for i in range(5):  # applying for loop to limit the number of choices
    choice = input()
    color.append(choice)

print("the list is as follows  :  ", color)
print("display first and last element of the list :  ", "\nfirst element is  :  ", color[0], "\nlast element is  :  ",
      color[-1])
