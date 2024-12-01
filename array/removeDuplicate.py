def removeDuplicates( nums):

  """
  Removes duplicate elements from a sorted array in-place.

  Args:
    nums: The input sorted array.

  Returns:
    The number of unique elements in the array.
  """
  l = 0 # Left pointer
  for r in range(1, len(nums)): # Right pointer iterates through the list
    if nums[l] != nums[r]: # If elements are different
      l += 1 # Move left pointer to the next position
      nums[l] = nums[r] # Replace the element at the left pointer
  return l + 1 # Return the index of the last unique element + 1(b/c l starts from 0)

num = [1, 2, 2, 3, 3]
print(removeDuplicates(num)) # Output: 3
print(num) # Output: [1, 2, 3, 3, 3] (the first 3 elements are unique)

 

        
