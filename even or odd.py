'''even or odd'''
def is_even(n):
    if n==0:
        return True
    else:
        return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    else:
        return is_even(n-1)
    
num=int(input("enter a num:"))
if is_even(num):
    print("even num",num)
else:
    print("odd num:",num)