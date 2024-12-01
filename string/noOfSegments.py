def countSegments( s):
    
    count = 0
    if any(char != ' ' for char in s):
            count = 1
    n = len(s)
    for i in range (n):
        
        if s[i] == " ":
            count +=1
    return count
 # correct answer  return len(s.split()) just this did you belive it
s = "   "
print(countSegments(s))
