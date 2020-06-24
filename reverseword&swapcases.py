#input a string
string=input()

#swapcase() method is used to swap all the cases in a string
str1= string.swapcase()

#split()method splits the words on identifying the spaces
str=str1.split()

#reversing the string "str" and joining it to print result
str=list(reversed(str))

print(" ".join(str))

