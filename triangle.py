'''no arg no return value'''
def hi():
    print("hi",end=" ")
    print("jashuva")
hi()


'''arg pass no return value'''
def hii(name):
    print("my name is",name)
str=input("enter:")
hii(str)

'''no arg pass return value'''
def num():
    return 100
x=num()
print(x)

'''arg pass return value'''
def sum(a,b):
    return a+b
n1=int(input("a:"))
n2=int(input("b:"))
res=sum(n1,n2)
print(res)

'''multiple args and multiple return'''
def info(name,age):
    return name,age
n=input("eter")
a=int(input("enter"))
resu=info(n,a)
print(n,a)