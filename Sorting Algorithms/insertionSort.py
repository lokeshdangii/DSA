def insertionSort(arr):
    n = len(arr)
    temp = int()
    j = int()
    for i in range(1,n):
        temp = arr[i]
        j = i-1

        while(j>=0 and arr[j]>temp):
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = temp
    
    return arr


arr = [8,4,5,1,9,2]
print(insertionSort(arr))