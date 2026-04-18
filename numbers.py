'''program to print the numbers from 1 to n using while loop'''
n = int(input("Enter the value of n: "))
i = 1
print("The even numbers from 1 to", n, "are:")
while i <= n:
    if i % 2 == 0:
        print(i, end=" ")
    i += 1
print("\nThe odd numbers from 1 to", n, "are:")
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i += 1
