class Solution(object):
    def partitionLabels(self, s): # time  o(n) + o(n) = o(n) space the same is rue
        """
        :type s: str
        :rtype: List[int]
        """
        last_occurence = {char: idx for idx, char in enumerate(s)}
        res = []

        l, r = 0, 0
        for idx, char in enumerate(s):
            r = max(r, last_occurence[char])

            if idx == r:
                res.append(r - l + 1)
                l = idx + 1
        return res