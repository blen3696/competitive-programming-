class Solution(object):
    def totalFruit(self, fruits):# o(n) o(n)
        """
        :type fruits: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        map = { }
        max_size = 0

        while r < len(fruits):
            map[fruits [r]] = 1 + map.get(fruits[r],0)
            while len(map) > 2:
                map[fruits[l]] -=1
                if map[fruits[l]] == 0:
                    map.pop(fruits[l])
                l +=1
            if len(map) <= 2:
                max_size = max(max_size, r - l +1)
                r +=1
        return max_size
           