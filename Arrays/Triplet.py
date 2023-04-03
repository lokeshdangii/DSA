'''# Given an integer array nums, return all the triplets [nums[i], nums[j], 
nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.'''

def triplets(nums):
    n = len(nums)
    list1 = []
  
    for i in range(0,n):
        for j in range(i+1,n): 
            for k in range(j+1,n):
                if i!=j and i!=k and j!=k and nums[i] + nums[j] + nums[k] == 0:
                    list1.append([nums[i], nums[j], nums[k]])
                    # return nums[i], nums[j], nums[k]
                    return list1
    return -1


# ------------------------------------------------------------------



def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j, k = i+1, len(nums)-1
        while j < k:
            total = nums[i] + nums[j] + nums[k]
            if total == 0:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k+1]:
                    k -= 1
            elif total < 0:
                j += 1
            else:
                k -= 1
    return result

# -------------------------------------------------------------------------------

def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        left, right = i+1, len(nums)-1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total < 0:
                left += 1
            elif total > 0:
                right -= 1
            else:
                res.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
    return res



# ---------------------------------------------------------------------------
nums = [-1, 0, 1, 2, -1, -4]
print(triplets(nums))
print(threeSum(nums))
