class Solution(object):
    def characterReplacement(self, s, k): #o(n) o(n)
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l =0
        r = 0
        max_len = 0
        Scount = {}

        while r < len(s):
            Scount[s[r]] = 1 + Scount.get(s[r],0)
            while (r - l + 1) - max(Scount.values()) > k:
                Scount[s[l]] -=1
                l +=1
                
            if  (r - l + 1) - max(Scount.values()) <= k:
                max_len = max(max_len, r - l + 1)   
                r +=1  
            
        return max_len