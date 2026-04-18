'''reverse a string without using built in functions'''
s = input("Enter a string: ")
rev = ""
for i in s:
    rev = i + rev
    print("The reverse of the string is:", rev)