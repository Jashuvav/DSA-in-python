#selection sort
'''Selection sort

29 71 98 12 86 66 52 51 36
T        L
12 71 98 29 86 66 52 51 36
   T     L
12 29 98 71 86 66 52 51 36
      T                 L
12 29 36 71 86 66 52 51 98
         T           L
12 29 36 51 86 66 52 71 98
            T     L
12 29 36 51 52 66 86 71 98
               T     L
12 29 36 51 52 66 86 71 98
                  T  L
12 29 36 51 52 66 71 86 98
                     L
                     T
12 29 36 51 52 66 71 86 98
                        L
                        T
Time complexity: O(n^2)
Space complexity: O(n)'''
arr=list(map(int, input("Enter the elements of the array: ").split()))
n=len(arr)
for i in range(n):
    min_idx=i
    for j in range(i+1, n):
        if arr[j]<arr[min_idx]:
            min_idx=j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
print("Sorted array is:", arr)
#dry run
#arr=[29,71,98,12,86,66,52,51,36]
#i=0; min_idx=0; j=1; arr[1]=71; arr[0]=29; 71<29? No -> min_idx=0
#i=0; min_idx=0; j=2; arr[2]=98; arr[0]=29; 98<29? No -> min_idx=0
#i=0; min_idx=0; j=3; arr[3]=12; arr[0]=29; 12<29? Yes -> min_idx=3
#i=0; min_idx=3; j=4; arr[4]=86; arr[3]=12; 86<12? No -> min_idx=3
#i=0; min_idx=3; j=5; arr[5]=66; arr[3]=12; 66<12? No -> min_idx=3
#i=0; min_idx=3; j=6; arr[6]=52; arr[3]=12; 52<12? No -> min_idx=3
#i=0; min_idx=3; j=7; arr[7]=51; arr[3]=12; 51<12? No -> min_idx=3
#i=0; min_idx=3; j=8; arr[8]=36; arr[3]=12; 36<12? No -> min_idx=3
#i=0; min_idx=3; swap -> arr=[12,71,98,29,86,66,52,51,36]
#i=1; min_idx=1; j=2; arr[2]=98; arr[1]=71; 98<71? No -> min_idx=1
#i=1; min_idx=1; j=3; arr[3]=29; arr[1]=71; 29<71? Yes -> min_idx=3
#i=1; min_idx=3; j=4; arr[4]=86; arr[3]=29; 86<29? No -> min_idx=3
#i=1; min_idx=3; j=5; arr[5]=66; arr[3]=29; 66<29? No -> min_idx=3
#i=1; min_idx=3; j=6; arr[6]=52; arr[3]=29; 52<29? No -> min_idx=3
#i=1; min_idx=3; j=7; arr[7]=51; arr[3]=29; 51<29? No -> min_idx=3
#i=1; min_idx=3; j=8; arr[8]=36; arr[3]=29; 36<29? No -> min_idx=3
#i=1; min_idx=3; swap -> arr=[12,29,98,71,86,66,52,51,36]
#i=2; min_idx=2; j=3; arr[3]=71; arr[2]=98; 71<98? Yes -> min_idx=3
#i=2; min_idx=3; j=4; arr[4]=86; arr[3]=71; 86<71? No -> min_idx=3
#i=2; min_idx=3; j=5; arr[5]=66; arr[3]=71; 66<71? Yes -> min_idx=5
#i=2; min_idx=5; j=6; arr[6]=52; arr[5]=66; 52<66? Yes -> min_idx=6
#i=2; min_idx=6; j=7; arr[7]=51; arr[6]=52; 51<52? Yes -> min_idx=7
#i=2; min_idx=7; j=8; arr[8]=36; arr[7]=51; 36<51? Yes -> min_idx=8
#i=2; min_idx=8; swap -> arr=[12,29,36,71,86,66,52,51,98]
#i=3; min_idx=3; j=4; arr[4]=86; arr[3]=71; 86<71? No -> min_idx=3
#i=3; min_idx=3; j=5; arr[5]=66; arr[3]=71; 66<71? Yes -> min_idx=5
#i=3; min_idx=5; j=6; arr[6]=52; arr[5]=66; 52<66? Yes -> min_idx=6
#i=3; min_idx=6; j=7; arr[7]=51; arr[6]=52; 51<52? Yes -> min_idx=7
#i=3; min_idx=7; j=8; arr[8]=98; arr[7]=51; 98<51? No -> min_idx=7
#i=3; min_idx=7; swap -> arr=[12,29,36,51,86,66,52,71,98]
#i=4; min_idx=4; j=5; arr[5]=66; arr[4]=86; 66<86? Yes -> min_idx=5
#i=4; min_idx=5; j=6; arr[6]=52; arr[5]=66; 52<66? Yes -> min_idx=6
#i=4; min_idx=6; j=7; arr[7]=71; arr[6]=52; 71<52? No -> min_idx=6
#i=4; min_idx=6; j=8; arr[8]=98; arr[6]=52; 98<52? No -> min_idx=6
#i=4; min_idx=6; swap -> arr=[12,29,36,51,52,66,86,71,98]
#i=5; min_idx=5; j=6; arr[6]=86; arr[5]=66; 86<66? No -> min_idx=5
#i=5; min_idx=5; j=7; arr[7]=71; arr[5]=66; 71<66? No -> min_idx=5
#i=5; min_idx=5; j=8; arr[8]=98; arr[5]=66; 98<66? No -> min_idx=5
#i=5; min_idx=5; swap -> arr=[12,29,36,51,52,66,86,71,98]
#i=6; min_idx=6; j=7; arr[7]=71
#i=6; min_idx=6; j=8; arr[8]=98; arr[6]=86; 98<86? No -> min_idx=6
#i=6; min_idx=6; swap -> arr=[12,29,36,51,52,66,86,71,98]
#i=7; min_idx=7; j=8; arr[8]=98; arr[7]=71; 98<71? No -> min_idx=7
#i=7; min_idx=7; swap -> arr=[12,29,36,51,52,66,86,71,98]
#i=8; min_idx=8; swap -> arr=[12,29,36,51,52,66,86,71,98]
