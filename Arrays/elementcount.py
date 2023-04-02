# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

def elecount(arr):
    count = 1

    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] != arr[j]:
                count += 0
            else:
                count += 1

    if count>=2:
        return True
    else:
        return False

arr = [1, 2, 4, 1,3]
print(elecount(arr))