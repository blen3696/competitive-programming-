def twoSumLessThanK(arr,k):
    l = 0
    r = len(arr) -1
    max_sum = 0
    arr.sort()
    while l < r:
        my_sum = arr[l] + arr[r]
        if my_sum < k:
            max_sum = max(max_sum,my_sum)
            l +=1
        else:
            r -=1
    return max_sum if max_sum !=0 else -1
nums =  [10,20,30]
k = 15
print(twoSumLessThanK(nums,k))
