'''2491. Divide Players Into Teams of Equal Skill
Solved
Medium
Topics
Companies
Hint
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
 '''
from collections import Counter

class Solution(object): #o(nlogn) +  o(n) = o(nlogn) , O(1)
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        n = len(skill)
        if n % 2 != 0:
           return -1
        total_skill = sum(skill)
        target_sum = total_skill // (n // 2)  

       # count = Counter(skill)
        chemistry = 0
       
        skill.sort() 
        l, r = 0, n-1
        while l < r:
            current_sum = skill[l] + skill[r]
            if current_sum == target_sum:
                chemistry += skill[l] * skill[r]
                l += 1
                r -= 1
            else:
                return -1 


        return chemistry


