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
    while n % 4 == 0:
        n //= 4
    return n == 1

# Example usage
print(is_power_of_three(64)) 