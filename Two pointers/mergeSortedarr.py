'''88. Merge Sorted Array

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should 
be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 '''
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        l = m -1
        r = n -1
        n = len(nums1) - 1

        
        while r >= 0 and l >= 0:
            if  nums1[l] >= nums2[r]:
                 nums1[n] = nums1[l]
                 l -=1
            else:
                 nums1[n] = nums2[r]
                 r -=1
            n -=1
        while r >= 0:
            nums1[n] = nums2[r]
            r -=1
            n -=1

        return nums1
    
    
    '''sort two arrays using additional space'''
    def mergearr(s, p):
        arr = []
        l = 0
        r = 0
        while l < len(s) and r < len(p):
            if s[l] <= p[r]:
                arr.append(s[l])
                l +=1
            else:
                arr.append(p[r])
                r +=1
        arr.extend(s[l:])
        arr.extend(p[r:])
        return arr
        
    s = [1,2,5,6]
    p = [3,4,7]
    print(mergearr(s,p))
