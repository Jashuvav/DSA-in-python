'''rotate the array 90 degree clockwise'''
'''rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
print("Enter the elements of the matrix:")
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
#transpose of the matrix
for i in range(rows):
    for j in range(i,cols):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#reverse each row
for i in range(rows):
    matrix[i].reverse()
print("The matrix after rotating 90 degree clockwise is:")
for row in matrix:
    print(*row)'''

'''rotate the array 90 degree anti-clockwise'''
rows=int(input("Enter the number of rows: "))
cols=int(input("Enter the number of columns: "))
matrix=[]
print("Enter the elements of the matrix:")
for i in range(rows):
    row=list(map(int,input().split()))
    matrix.append(row)
#transpose of the matrix
for i in range(rows):
    for j in range(i,cols):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
#reverse each column
for i in range(cols):
    for j in range(rows//2):
        matrix[j][i],matrix[rows-1-j][i]=matrix[rows-1-j][i],matrix[j][i]
print("The matrix after rotating 90 degree anti-clockwise is:")
for row in matrix:
    print(*row)
