def eleSearch(arr,target):
    left,right = 0, len(arr)-1
    mid = 0
    while left<right:
        mid = (left+right)//2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
            if arr[left] == target:
                return left
        else:
            right= mid -1
            if arr[right] == target:
                return right
    
    return -1
        

arr = [1,2,4,5,8,9,]
# arr = [4, 5, 6, 7, 0, 1, 2]
target = 5
print(eleSearch(arr,target))
