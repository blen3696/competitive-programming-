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