'''3206. Alternating Groups I

There is a circle of red and blue tiles. You are given an array of integers colors.
The color of tile i is represented by colors[i]:

colors[i] == 0 means that tile i is red.
colors[i] == 1 means that tile i is blue.
Every 3 contiguous tiles in the circle with alternating colors (the middle tile has a different 
color from its left and right tiles) is called an alternating group.

Return the number of alternating groups.

Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

Example 1:

Input: colors = [1,1,1]

Output: 0

Explanation:



Example 2:

Input: colors = [0,1,0,0,1]

Output: 3

Explanation:



Alternating groups:



 

Constraints:

3 <= colors.length <= 100
0 <= colors[i] <= 1'''
class Solution(object):
    def numberOfAlternatingGroups(self, colors):
        """
        :type colors: List[int]
        :rtype: int
        """
        l = 0
        n = len(colors)
        alt_group = 0

        if colors[0] == 0:
            if colors[n-1] == 1 and colors[1] == 1:
                alt_group +=1
        if colors[0] == 1:
            if colors[n-1] == 0 and colors[1] == 0:
                alt_group +=1
                
                

        for r in range(1,n-1):
            if colors[r] == 0:
                 if colors[l] == 1 and colors[r+1] == 1:
                     alt_group +=1
            if colors[r] == 1:
                 if colors[l] == 0 and colors[r+1] == 0:
                     alt_group +=1
            l+=1
            
            
        if colors[n-1] == 0:
            if colors[n-2] == 1 and colors[0] == 1:
                alt_group +=1
        if colors[n-1] == 1:
            if colors[n-2] == 0 and colors[0] == 0:
                alt_group +=1

        return alt_group