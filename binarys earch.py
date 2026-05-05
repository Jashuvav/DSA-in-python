'''binary search'''
arr=list(map(int, input("Enter the elements of the array (sorted): ").split()))
target=int(input("Enter the target element: "))
low=0
high=len(arr)-1
found=False
while low<=high:
    mid=(low+high)//2
    if arr[mid]==target:
        print("Element found at index:", mid)
        found=True
        break
    elif arr[mid]<target:
        low=mid+1
    else:
        high=mid-1
if not found:
    print("Element not found in the array.")

#dry run
#arr=[1,2,3,4,5]; target=3
#low=0; high=4; mid=(0+4)//2=2; arr[2]=3; 3==3? Yes -> print("Element found at index:", 2); found=True; break