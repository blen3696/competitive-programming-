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


