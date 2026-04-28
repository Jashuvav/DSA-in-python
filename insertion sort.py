#selection sort
arr=list(map(int, input("Enter the elements of the array: ").split()))
n=len(arr)
for i in range(n):
    key = arr[i]
    j = i-1
    while j>=0 and arr[j]>key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Sorted array is:", arr)
#dry run
#arr=[29,71,98,12,86,66,52,51,36]
#i=0; key=29; j=-1; arr[0]=29; arr[-1]=36; 29>36? No -> arr[0]=29
#i=1; key=71; j=0; arr[1]=71; arr[0]=29; 71>29? No -> arr[1]=71
#i=2; key=98; j=1; arr[2]=98; arr[1]=71; 98>71? No -> arr[2]=98
#i=3; key=12; j=2; arr[3]=12; arr[2]=98; 12>98? No -> arr[3]=98; j=1; arr[2]=12; arr[1]=71; 12>71? No -> arr[2]=71; j=0; arr[1]=12; arr[0]=29; 12>29? No -> arr[1]=29; j=-1; arr[0]=12
#i=4; key=86; j=3; arr[4]=86; arr[3]=98; 86>98? No -> arr[4]=98; j=2; arr[3]=86; arr[2]=71; 86>71? No -> arr[3]=71; j=1; arr[2]=86; arr[1]=29; 86>29? No -> arr[2]=29; j=0; arr[1]=86; arr[0]=12; 86>12? No -> arr[1]=12
#i=5; key=66; j=4; arr[5]=66; arr[4]=98; 66>98? No -> arr[5]=98; j=3; arr[4]=66; arr[3]=86; 66>86? No -> arr[4]=86; j=2; arr[3]=66; arr[2]=29; 66>29? No -> arr[3]=29; j=1; arr[2]=66; arr[1]=12; 66>12? No -> arr[2]=12; j=0; arr[1]=66; arr[0]=12; 66>12? No -> arr[1]=12
#i=6; key=52; j=5; arr[6]=52; arr[5]=98; 52>98? No -> arr[6]=98; j=4; arr[5]=52; arr[4]=86; 52>86? No -> arr[5]=86; j=3; arr[4]=52; arr[3]=29; 52>29? No -> arr[4]=29; j=2; arr[3]=52; arr[2]=12; 52>12? No -> arr[3]=12; j=1; arr[2]=52; arr[1]=12; 52>12? No -> arr[2]=12
#i=7; key=51; j=6; arr[7]=51; arr[6]=98; 51>98? No -> arr[7]=98; j=5; arr[6]=51; arr[5]=86; 51>86? No -> arr[6]=86; j=4; arr[5]=51; arr[4]=29; 51>29? No -> arr[5]=29; j=3; arr[4]=51; arr[3]=12; 51>12? No -> arr[4]=12; j=2; arr[3]=51; arr[2]=12; 51>12? No -> arr[3]=12
#i=8; key=36; j=7; arr[8]=36; arr[7]=98; 36>98? No -> arr[8]=98; j=6; arr[7]=36; arr[6]=86; 36>86? No -> arr[7]=86; j=5; arr[6]=36; arr[5]=29; 36>29? No -> arr[6]=29; j=4; arr[5]=36; arr[4]=12; 36>12? No -> arr[5]=12; j=3; arr[4]=36; arr[3]=12; 36>12? No -> arr[4]=12
#i=8; key=36; j=2; arr[4]=36; arr[2]=12; 36>12? No -> arr[3]=12; j=1; arr[3]=36; arr[1]=12; 36>12? No -> arr[2]=12; j=0; arr[2]=36; arr[0]=12; 36>12? No -> arr[1]=12
#output
#Enter the elements of the array: 29 71 98 12 86 66 52 51 36
#Sorted array is: [12, 29, 36, 51, 52, 66, 86, 98]