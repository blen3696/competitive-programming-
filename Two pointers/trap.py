class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r = 0, len(height)-1
        left_max, right_max = 0, 0
        water = 0
        while l <= r:
            if height[l] <  height[r]:
                if height[l] > left_max:
                    left_max = height[l]
                else:
                    water += left_max - height[l]
                l +=1
            else:
                if height[r] > right_max:
                    right_max = right_max
                else:
                    water += right_max - height[r]
                r -= 1
        return water

