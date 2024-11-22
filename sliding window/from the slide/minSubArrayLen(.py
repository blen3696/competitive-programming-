def minSubArrayLen( target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        min_len = 0
        sum = 0
        n = len(nums)
        while r < n:
             sum += nums[r]
             while sum >= target:
                 min_len = min(min_len, r - l + 1)  #Record shortest length
                 sum -= nums[l]  #Shrink window
                 l += 1
             r += 1  
           
        return min_len if min_len != float('inf') else 0 
target = 7
nums = [2,3,1,2,4,3]
    
print(minSubArrayLen(target,nums))
