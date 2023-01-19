# Program to create a string from the given string where first and last characters are exchanged
word = "PYTHON"
first = 'PYTHON'[0]
second = 'PYTHON'[1:-1]
last = 'PYTHON'[-1]
newWord = last + second + first
print("Newly formed word after swapping  :  ", newWord)
