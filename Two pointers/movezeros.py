def moveNonZeroes(nums):
    holder = 0
    seeker = 0
    while seeker < len(nums):
        if nums[seeker] != 0:
            temp = nums[holder]  
            nums[holder] = nums[seeker]  
            nums[seeker] = temp  
            holder += 1
        seeker += 1