#program to enter the name,marks of five subjects & calculate total marks and percentage

name=input("enter your name   : ")
mark1=int(input("Enter marks of Botany  : "))
mark2=int(input("Enter marks of Chemistry  : "))
mark3=int(input("Enter marks of Physics  : "))
mark4=int(input("Enter marks of Mathematics  : "))
mark5=int(input("Enter marks of Zoology  : "))

total=mark1+mark2+mark3+mark4+mark5
print("Total marks   : ",total,"/500")
percentage=(total/500)*100
print("percentage  : ",percentage,"%")
