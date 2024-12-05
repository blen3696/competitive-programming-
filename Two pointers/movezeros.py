'''283. Move Zeroes
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 '''
def moveNonZeroes(nums):
    holder = 0
    seeker = 0
    while seeker < len(nums):
        if nums[seeker] != 0:
            nums[holder], nums[seeker] = nums[seeker], nums[holder]
            holder += 1
        seeker += 1