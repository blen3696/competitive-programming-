def longestSubstring(s: str):
    charSet = set()
    l = 0
    max_len = 0
    
    for r in range(len(str)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l+=1
        charSet.add(s[r])
        max_len = max(max_len,r-l+1)
    return max_len