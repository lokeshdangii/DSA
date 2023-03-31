arr = [2,4,6,8,10]
tp = 0
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        print("({},{})".format(arr[i],arr[j]),end=" ")
        tp +=1
    print()

print("Total Pairs = ",tp)
