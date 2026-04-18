arr=list(map(int,input("Enter the array elements: ").split()))
k=int(input("Enter the difference target: "))
pairs=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if abs(arr[i]-arr[j])==k:
            print(f"Pair found: {arr[i]} and {arr[j]} with difference {k}")
            pairs=True
if not pairs:
    print("No pairs found with the specified difference.")