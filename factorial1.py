'''factorial in indirect '''
def one(n):
    if n==0 or n==1:
        return 1
    else:
        return n*one(n-1)
def two(n):
    if n==0 or n==1:
        return 1
    else:
        return n*two(n-1)
    
num=int(input("enter a num:"))
print(one(num))