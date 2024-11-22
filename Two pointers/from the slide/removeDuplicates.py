class Solution(object):
    def removeDuplicates(self, arr):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(1, len(arr)):
              if arr[i] != arr[j]:
                 i += 1
                 arr[i] = arr[j]
        return i + 1