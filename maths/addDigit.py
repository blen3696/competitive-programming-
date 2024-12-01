def addDigit(x):
  """
  Repeatedly adds the last digit of a number to itself until it becomes a single digit.

  Args:
    x (int): The input number.

  Returns:
    int: The resulting single-digit number.
  """

  number = x
  while number > 9:
    sum_digits = 0
    while number > 0:
      digit = number % 10
      sum_digits += digit
      number //= 10 # Integer division to remove the last digit
    number = sum_digits # Update the number with the sum of digits
  return number

num = 32
print(addDigit(num)) # Output: 5
