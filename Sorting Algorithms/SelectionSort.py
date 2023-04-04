def selectionSort(arr):
    minPos = 0

    for i in range(0,len(arr)-1):
        minPos = i
        for j in range(i+1,len(arr)):
            if arr[minPos] > arr[j]:
                minPos = j
        

        arr[minPos],arr[i] = arr[i],arr[minPos]
    

    return arr


arr = [5,4,1,2,3]
print(selectionSort(arr))
