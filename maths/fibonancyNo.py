def fibonacci(n):
  """
  Calculates the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to calculate (starting from 0).

  Returns:
    The nth Fibonacci number.
  """
  if n <= 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)


x = 3
print(fibonacci(x))