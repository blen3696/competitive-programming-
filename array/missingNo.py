def missingNumber(nums):
  """
  Finds the missing number in a range of numbers from 0 to n.

  Args:
    nums: An array containing n distinct numbers in the range [0, n].

  Returns:
    The missing number in the range.
  """
  n = len(nums)
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

# Example usage:
nums = [3, 0, 1]
missing_number = missingNumber(nums)
print(f"The missing number is: {missing_number}")

    
