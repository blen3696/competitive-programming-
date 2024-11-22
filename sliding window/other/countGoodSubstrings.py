class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        Scount = {}
        good_sub = 0
        if len(s) < 3:
            return 0
        for i in range(3):
            Scount[s[i]] = 1 + Scount.get(s[i],0)
        if all(count == 1 for count in Scount.values()):
             good_sub +=1
        for r in range(3, len(s)):
             Scount[s[r]] = 1 + Scount.get(s[r],0)
             Scount[s[l]] -=1
             if Scount[s[l]] == 0:
                 Scount.pop(s[l])
             l+=1
             if all(count == 1 for count in Scount.values()):
                 good_sub +=1
        return good_sub

