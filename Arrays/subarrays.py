arr = [2,4,6,8,10]
ts = 0
sum = 0
sumlist = []
for i in range(0,len(arr)):
    
    for j in range(i,len(arr)):
        sum = 0
        for k in range(i,j+1):
            sum += arr[k]
            print(arr[k], end=" ")

        print("\nsum of array :",sum)
        sumlist.append(sum)
            
        ts +=1
        print()
    print()

print("Total Subarrays :", ts)
print("The minimum sum of subarray :", min(sumlist))
print("The maximum sum of subarray :", max(sumlist))