#A palindrome is a number that reads the same backward as forward.
import math


def isPalindrome( x):
    y = x
    rev_no = 0
    
    while x > 0:
        
        z = x % 10
        rev_no = (rev_no*10) + z
        x = x // 10
    
    if  rev_no== y:
        return True
    else:
        return False

x = 121
print(isPalindrome(x))
        