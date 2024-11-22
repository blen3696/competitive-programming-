class Solution(object):
    def maxArea(self, height):#o(n), o(1)
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0 
        r = len(height) - 1
        max_area = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            max_area = max(max_area, area)

            if height[r] <= height[l]:
                r -=1
            else:
                l +=1
        return max_area
