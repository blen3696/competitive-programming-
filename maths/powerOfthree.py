def is_power_of_three(n):
    """
    Checks if an integer is a power of three.

    Args:
        n (int): The integer to check.

    Returns:
        bool: True if n is a power of three, False otherwise.
    """
    if n <= 0:
        return False
    while n % 3 == 0:
        n //= 3
    return n == 1

# Example usage
print(is_power_of_three(27))  # Output: True
print(is_power_of_three(9))   # Output: True
print(is_power_of_three(45))  # Output: False
print(is_power_of_three(0))   # Output: False
print(is_power_of_three(1))   # Output: True

