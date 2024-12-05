'''633. Sum of Square Numbers
Solved
Medium
Topics
Companies
Given a non-negative integer c, decide whether there're two integers a and b such that a2 + b2 = c.

 

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:

Input: c = 3
Output: false
 '''
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