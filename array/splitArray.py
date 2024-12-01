def isPossibleToSplit( nums):
   
    frequencies = {}
    for element in nums:
         if element in frequencies:
             frequencies[element] += 1
         else:
             frequencies[element] = 1
    
    for element, frequency in frequencies.items():
         if frequency > 2:
             return False

    return True
nums = [1,1,2,2,3,4,1]
print(isPossibleToSplit(nums))