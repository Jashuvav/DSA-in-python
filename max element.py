'''program to find the maximum element in an array without using built-in functions'''
'''arr=list(map(int,input("Enter the array elements: ").split()))
max_element=arr[0]
for num in arr:
    if num>max_element:
        max_element=num
print(f"The maximum element in the array is: {max_element}")'''


'''program to find the maximum element in an 2D array '''
'''rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
for i in range(rows):
    row=list(map(int,input(f"Enter the elements of row {i+1}: ").split()))
    matrix.append(row)  
max_element=matrix[0][0]
for i in range(rows):
    for j in range(cols):
        if matrix[i][j]>max_element:
            max_element=matrix[i][j]
print(f"The maximum element in the 2D array is: {max_element}")

'''write a program to traverse an array and print all the even values and odd values separately'''
arr=list(map(int,input("Enter the array elements: ").split()))
even_values=[]
odd_values=[]
for num in arr:
    if num%2==0:
        even_values.append(num)
    else:
        odd_values.append(num)
print(f"The even values in the array are: {even_values}")
print(f"The odd values in the array are: {odd_values}")

''' write a code to sort a list of strings based on the len and print the sorted arr without using built-in functions'''
strings=list(map(str,input("Enter the strings: ").split()))
n=len(strings)
for i in range(n):
    for j in range(i+1,n):
        if len(strings[j])<len(strings[j+1]):
            strings[j],strings[j+1]=strings[j+1],strings[j]
print(f"The sorted strings based on length are: {strings}")

'''write a program to count they repeted elements count'''
arr=list(map(int,input("Enter the array elements: ").split()))
count_dict=[]
for num in arr:
    if num in count_dict:
        count_dict[num]+=1
    else:
        count_dict[num]=1
count=0
for values in count_dict.values():
    if values>1:
        count+=1    
    print(f"Element: {num}, Count: {count}")

'''output for the above code is:'''
'''Enter the array elements: 1 2 3 4 5 2 3
Element: 1, Count: 0
Element: 2, Count: 2
Element: 3, Count: 2
Element: 4, Count: 0
Element: 5, Count: 0
The total number of repeated elements is: 2
'''
'''dry run for the above code:'''
'''Enter the array elements: 1 2 3 4 5 2 3
num=1, count_dict={1:1}
num=2, count_dict={1:1, 2:1}
num=3, count_dict={1:1, 2:1, 3:1}
num=4, count_dict={1:1, 2:1, 3:1, 4:1}
num=5, count_dict={1:1, 2:1, 3:1, 4:1, 5:1}
num=2, count_dict={1:1, 2:2, 3:1, 4:1, 5:1}
num=3, count_dict={1:1, 2:2, 3:2, 4:1, 5:1}'''