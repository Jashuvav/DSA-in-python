'''program to reverse a num using math approach'''
n = int(input("Enter a number: "))
rev = 0
while n!= 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("The reverse of the number is:", rev)
