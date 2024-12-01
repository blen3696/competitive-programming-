class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pri_sum = [0]
        for num in nums:
            pri_sum.append(pri_sum[-1] + num)
        for i in range(len(pri_sum)-1):
            l_sum = pri_sum[i]
            r_sum = pri_sum[-1] - pri_sum[i+1]
            if l_sum == r_sum:
                return i
        return -1