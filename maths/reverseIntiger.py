def reverse(x):
    """Reverses the digits of a signed 32-bit integer x, handling the overflow
    condition.

    Args:
        x: The integer to reverse.

    Returns:
        The reversed integer if it stays within the 32-bit range, otherwise 0.
    """
    is_negative = x < 0
    x = abs(x)

    rev_no = 0
    while x > 0:
        z = x % 10
        rev_no = (rev_no * 10) + z
        x //= 10

    # Check for overflow before restoring the sign we can only alloed to use 32 bits
    if rev_no > 2**31 - 1:
        return 0

    if is_negative:
        rev_no = -rev_no

    return rev_no

x = 1534236469
print(reverse(x))  # Output: 0 (overflow)
x = -12034500
print(reverse(x))  # Output: -543021



