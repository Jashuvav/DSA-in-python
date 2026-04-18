'''find the pair sum for a given data and print the possible pairs using bruteforce'''
#arr[2,4,6,8] target = 10
arr=list(map(int,input("Enter the array elements: ").split()))
target=int(input("Enter the target sum: "))
pairs=False
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(f"Pair found: {arr[i]} + {arr[j]} = {target}")
            pairs=True
if not pairs:
    print("No pairs found that sum to the target.")


'''naive approach'''
arr=list(map(int,input("Enter the array elements: ").split()))
target=int(input("Enter the target sum: "))

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print(f"Pair found: {arr[i]} + {arr[j]} = {target}")
        
'''math apporach hashing apporach'''
arr=list(map(int,input("Enter the array elements: ").split()))
target=int(input("Enter the target sum: "))
seen=set()
found=False
for num in arr:
    complement=target-num
    if complement in seen:
        print(f"Pair found: {num} + {complement} = {target}")
        found=True
    seen.add(num)
if not found:
    print("not found:")
            
