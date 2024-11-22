class Solution(object):
    def equalSubstring(self, s, t, maxCost):# o(n) o(1)
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        l = 0
        r = 0
        total_cost = 0
        max_len = 0
        while r < len(s):
            cost = abs(ord(s[r]) - ord(t[r]))
            total_cost = total_cost + cost
            while total_cost > maxCost:
                total_cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
            max_len = max(max_len,r-l+1)
            r += 1
            
        return max_len
