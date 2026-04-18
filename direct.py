'''direct recurision'''
def natural(num):
    if num==0:
        return
    print(num,end=" ")
    natural(num-1)
num=int(input("enter:"))
natural(num)
