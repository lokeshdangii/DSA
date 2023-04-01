arr = [1,-2,6,-1,3]
curr_sum = 0
maxsum = -10000

for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        curr_sum = 0
        for k in range(i,j+1):
           curr_sum += arr[k]
        # print("Current Sum of Subarray = ",curr_sum)

        if maxsum < curr_sum:
            maxsum = curr_sum

print("Maximum Sum = ",maxsum)

