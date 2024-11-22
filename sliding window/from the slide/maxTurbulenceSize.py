class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l = 0
        r = 1
        max_size = 1
        char = ' '
       


        while r < len(arr):
            if arr[r - 1] > arr[r] and char != '>':
                     max_size = max( max_size, r -l + 1)
                     r +=1
                     char = '>'
                    
            elif arr[r - 1] < arr[r] and char != '<':
                     max_size = max( max_size, r -l + 1)
                     r +=1
                     char = '<' 
            else:
                 r = r + 1 if arr[r] == arr[r - 1] else r
                 l = r -1
                 char = ' '

                  

        return max_size

           