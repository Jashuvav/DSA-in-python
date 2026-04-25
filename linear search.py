#linear search
arr=list(map(int, input("Enter the elements of the array: ").split()))
target=int(input("Enter the target element: "))
found=False
for i in range(len(arr)):
    if arr[i]==target:
        print("Element found at index:", i)
        found=True
        break
if not found:
    print("Element not found in the array.")

#dry run
#arr=[1,2,3,4,5]; target=3
#i=0; arr[0]=1; 1==3? No
#i=1; arr[1]=2; 2==3? No
#i=2; arr[2]=3; 3==3? Yes -> print("Element found at index:", 2); found=True; break

#output
#Enter the elements of the array: 1 2 3 4 5
#Enter the target element: 3
#Element found at index: 2

