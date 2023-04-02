height = [4,2,0,6,3,2,5]
n = len(height)
left_maxBoundary = [0]*n
right_maxBoundary = [0]*n

left_maxBoundary[0] = height[0]
right_maxBoundary[n-1] = height[n-1]

max = height[0]

for i in range(1,n):
    if max < height[i]:
        max = height[i]
        left_maxBoundary[i] = max
    else:
        left_maxBoundary[i] = max

print(left_maxBoundary)

max = height[n-1] # initializing last element of heigth to the max

for i in range(n-2,-1,-1):
    if max<height[i]:
        max = height[i]
        right_maxBoundary[i] = max
    else:
        right_maxBoundary[i] = max

print(right_maxBoundary)

min_value = 0
traped_water = 0

for i in range(0,n-1):
    min_value = min(left_maxBoundary[i],right_maxBoundary[i])
    traped_water += min_value - height[i]


print("Total water trapped : ",traped_water)
