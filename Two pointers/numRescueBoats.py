'''881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number
of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at
the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.

 

Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)
 '''

class Solution(object):
    def numRescueBoats(self, people, limit): #o(nlogn) +  o(n) = o(nlogn) , O(1)
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()
        l = 0 
        r = len(people) - 1
        boat = 0

        while l <= r:  
            if people[l] + people[r] <= limit:
                l +=1
                r -=1
            else:
                r -=1
            boat +=1
            
        return boat 