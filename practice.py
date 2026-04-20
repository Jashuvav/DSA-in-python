#[1,0,0,5,0,3] -> [1,5,3,0,0,0]
'''write a program to move all the zeroes in an array to the end of the list '''
arr=list(map(int,input("Enter the array elements: ").split()))
non_zero_index=0
for i in range(len(arr)):
    if arr[i]!=0:
        arr[non_zero_index]=arr[i]
        non_zero_index+=1
for i in range(non_zero_index,len(arr)):
    arr[i]=0
print(f"The array after moving zeroes to the end is: {arr}")
