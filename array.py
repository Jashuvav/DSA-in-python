'''program to fetch a value from an array for constant optimization'''
'''def value(arr):
    return arr[-3]
arr=list(map(int,input("enter").split()))
print(value(arr))'''
#output
'''enter1 2 3 4 5
    3'''

'''def value(arr):
    for i in arr:
        print(i+10 ,end=" ")
arr=list(map(int,input("enter").split()))
value(arr)'''
#output
'''enter1 2 3
11 12 13'''

'''def pairs(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            print(arr[i],arr[j])
arr=list(map(int,input("enter").split()))
pairs(arr)'''

#output
'''enter1 2 3
1 1
1 2
1 3
2 1
2 2
2 3
3 1
3 2
3 3'''

'''program to find the steps of exponiational formate of a given num where the logorithmitic optimization refelets'''
def power(x,n):
    result=1
    steps=0
    while n!=0:
        steps+=1
        print(f"steps{steps} : x={x} n={n} result={result}")
        if n%2==1:
            result*=x
        x*=x
        n//=2
        print("final result",result)
        print("total steps",steps)
base=int(input("enter base"))
exponent=int(input("enter exponent"))
power(base,exponent)