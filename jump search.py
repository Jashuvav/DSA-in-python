'''jump search'''
import math
arr=list(map(int, input("Enter the elements of the array (sorted): ").split()))
target=int(input("Enter the target element: "))
n=len(arr)
step=int(math.sqrt(n))
prev=0
found=False
while prev<n and arr[min(step, n)-1]<target:
    prev=step
    step+=int(math.sqrt(n))
    if prev>=n:
        break
    for i in range(prev, min(step, n)):
        if arr[i]==target:
            print("Element found at index:", i)
            found=True
            break
if not found:
    print("Element not found in the array.")  