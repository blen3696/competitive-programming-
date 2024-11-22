
def minSubArrayLen( target, nums): # o(n) o(1)
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        l = 0 
        r = 0
        min_len = float('inf')
        sum = 0
        n = len(nums)
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
               min_len = min(min_len, r - l + 1)
               sum = sum-nums[l]
               l +=1
        return min_len if min_len != float('inf') else 0 
target = 7 
nums = [2,1,1,0,0,1]
print(minSubArrayLen(target,nums))