'''traversal of 2D arrays

      top
      1   2  3 4
left  12 13 14 5
      11 16 15 6  right
      10  9  8 7 
       bottom         '''
n = int(input("Enter the size: "))
matrix = [[0]*n for _ in range(n)]
top = 0
bottom = n-1
left = 0
right = n-1
num = 1
while top<=bottom and left<=right:
   #left -> right (top)
   for i in range(left, right+1):
      matrix[top][i] = num
      num += 1
   top += 1
   #top -> bottom (right)
   for i in range(top, bottom+1):
      matrix[i][right] = num
      num += 1
   right -= 1
   #right -> left (bottom)
   for i in range(right, left-1, -1):
      matrix[bottom][i] = num
      num += 1
   bottom -= 1
   #bottom -> top (left)
   for i in range(bottom, top-1, -1):
      matrix[i][left] = num
      num += 1
   left += 1
print("Spiral pattern clock-wise: ")
for row in matrix:
   print(*row)