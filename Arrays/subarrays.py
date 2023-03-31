arr = [2,4,6,8,10]

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        for k in range(i,j+1):
            print(arr[k],end=" ")
        print()
    print()