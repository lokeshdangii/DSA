#  Program to find maximum sum of subarrays of an arrray

def bruteforce(arr):
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

def kadensAlgo(arr):
    curr_sum = 0
    max_sum = -1000000

    for i in range(0,len(arr)):
        curr_sum += arr[i]

        if curr_sum <0:
            curr_sum = 0
        
        if curr_sum>max_sum:
            max_sum = curr_sum
    
    print("Maximum Sum = ",max_sum)


arr = [1,-2,6,-1,3]
arr1 = [-2,-3,4,-1,-2,1,5,-3]
# bruteforce(arr)
kadensAlgo(arr1)


