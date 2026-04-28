#bubble sort
#values 3 2 4 1 5 8 0 6
'''
pass-1
3 2 4 1 5 8 0 6
2 3 4 1 5 8 0 6
2 3 1 4 5 8 6 0
2 3 1 4 5 0 6 8

pass-2
2 3 1 4 5 0 6 8
2 1 3 4 5 0 6 8
2 1 3 4 0 5 6 8

pass-3
2 1 3 4 0 5 6 8
1 2 3 4 0 5 6 8
1 2 3 0 4 5 6 8

pass-4
1 2 3 0 4 5 6 8
1 2 0 3 4 5 6 8

pass-5
1 2 0 3 4 5 6 8
1 0 2 3 4 5 6 8

pass-6
1 0 2 3 4 5 6 8
0 1 2 3 4 5 6 8

Time complexity: O(n^2)
Space complexity: O(n)'''
arr=list(map(int, input("Enter the elements of the array: ").split()))
n=len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted array is:", arr)

#dry run
#arr=[3,2,4,1,5,8,0,6]
#i=0; j=0; arr[0]=3; arr[1]=2; 3>2? Yes -> swap -> arr=[2,3,4,1,5,8,0,6]
#i=0; j=1; arr[1]=3; arr[2]=    4; 3>4? No -> no swap -> arr=[2,3,4,1,5,8,0,6]
#i=0; j=2; arr[2]=4; arr[3]=1; 4>1? Yes -> swap -> arr=[2,3,1,4,5,8,0,6]    
#i=0; j=3; arr[3]=4; arr[4]=5; 4>5? No -> no swap -> arr=[2,3,1,4,5,8,0,6]
#i=0; j=4; arr[4]=5; arr[5]=8; 5>8? No -> no swap -> arr=[2,3,1,4,5,8,0,6]
#i=0; j=5; arr[5]=8; arr[6]=0; 8>0? Yes -> swap -> arr=[2,3,1,4,5,0,6,8]
#i=0; j=6; arr[6]=6; arr[7]=8; 6>8? No -> no swap -> arr=[2,3,1,4,5,0,6,8]

