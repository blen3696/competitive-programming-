class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pri_sum = []
        acc = 0
        for i in range(len(nums)):
            acc += nums[i]
            pri_sum.append(acc)
        return pri_sum
