class Solution(object):# o(n) o(n)
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool  
        """
        arr = []
        for i in range(0,int(c ** 0.5) + 1):
            arr.append(i)
        l, r = 0, len(arr)-1
        while l <= r:
            sq = arr[l] ** 2 + arr[r] ** 2
            if sq == c:
                return True

            elif sq > c:
                 r -=1
            else:
                 l +=1
        return False