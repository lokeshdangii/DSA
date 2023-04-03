def trappingRainwater(height):

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

    water_level = 0   
    traped_water = 0

    for i in range(0,n-1):
        water_level = min(left_maxBoundary[i],right_maxBoundary[i])
        traped_water += water_level - height[i]

    return traped_water
    

height = [4,2,0,6,3,2,5]
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
tw = trappingRainwater(height)
print("Total water trapped : ",tw)