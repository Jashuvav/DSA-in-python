#merge sort
'''                                15 5 24 8 1 3 16 10 20     
                                /                               \
                            15 5 24 8                         1 3 16 10 20
                            /           \                         /           \
                          15 5         24 8                     1 3 16     10 20
                          /   \         /   \                   /   \         /   \
                         15   5       24   8                 1     3     16     10 20
                         / \   / \     / \   / \               / \   / \     / \     / \
                        15 15  5  5   24 24  8  8             1   1  3  3   16 16   10 10   20 20
                        \ /   \ /     \ /   \ /               \ /   \ /     \ /     \ /     \ /
                         15    5       24    8                 1     3       16     10      20
                          \   /         \   /                   \   /         \    /         \
                           15            8                     1             10             20
                            \           /                       \           /
                             15        8                         1         10
                              \      /                             \      /
                               15   8                               1   10
                                \ /
                                 15
Time complexity: O(n log n)
Space complexity: O(n)'''
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)
def merge(left,right):
    result=[]
    i=0
    j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result +=left[i:]
    result+=right[j:]
    return result
arr=list(map(int,input("enter ele:").split()))
sorted_arr=merge_sort(arr)
print(sorted_arr)
#dry run:

#arr=[15,5,24,8,1,3,16,10,20]
#mid=4
#left=[15,5,24,8]
#right=[1,3,16,10,20]