'''209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 '''
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