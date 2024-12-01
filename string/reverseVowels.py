def reverse_string(s):
   
    s = list(s)
    left = 0
    right = len(s) - 1
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    
    while left < right:
        if s[left] in vowels:
            if s[right] in vowels:
                temp = s[left]
                s[left] = s[right]
                s[right] = temp
                left += 1
                right -= 1
            else:
                right -= 1
        else:
            if s[right] in vowels:
                left += 1
            else:
                left += 1
                right -= 1
    
    return ''.join(s)

# Example usage
string = "leetcode"
reversed_string = reverse_string(string)
print(reversed_string)  # Output: !dlroW ,olleH
