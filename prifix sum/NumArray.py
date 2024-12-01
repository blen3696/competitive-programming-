class NumArray:

    def __init__(self, nums: List[int]):
      self.pri_sum = [0]
      for num in nums:
        self.pri_sum.append(self.pri_sum[-1]+ num)

    def sumRange(self, left: int, right: int) -> int:
        l = self.pri_sum[left]
        r = self.pri_sum[right+1]
       
        return r - l