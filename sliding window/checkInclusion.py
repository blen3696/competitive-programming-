'''567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.'''
def checkInclusion( p, s):
    
    Pcount = {}
    Scount = {}
   
    for i in range(len(p)):
        Pcount[p[i]] = 1 + Pcount.get(p[i],0)
        Scount[s[i]] = 1 + Scount.get(s[i],0)
    if Pcount == Scount:
        return True
    
    l =0
    for r in range(len(p), len(s)):
        Scount[s[r]] = 1 + Scount.get(s[r],0)
        Scount[s[l]] -=1
        if Scount[s[l]] == 0:
            Scount.pop(s[l])
        
        l+=1
        
        if Scount == Pcount:
            return True
    return False
s1 = "hello"
s2 = "ooolleoooleh"
print(checkInclusion(s1,s2))