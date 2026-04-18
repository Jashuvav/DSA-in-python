'''full right angle triangle pattern'''
n=int(input("Enter the number of rows: "))
for i in range(n):
    for j in range(i):
       print("*", end=" ")
    print()