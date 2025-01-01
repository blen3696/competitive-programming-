'''438. Find All Anagrams in a String

Given two strings s and p, return an array of all the start indices of p's 
anagrams in s. You may return the answer in any order.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".'''
def findAnagrams(self, s, p): # o(n) o(n)
    if len(p) > len(s): return []
    Pcount = {}
    Scount = {}
   
    for i in range(len(p)):
        Pcount[p[i]] = 1 + Pcount.get(p[i],0)
        Scount[s[i]] = 1 + Scount.get(s[i],0)
    if Pcount == Scount:
        res = [0]
    else:
        res = []
    l =0
    for r in range(len(p), len(s)):
        Scount[s[r]] = 1 + Scount.get(s[r],0)
        Scount[s[l]] -=1
        if Scount[s[l]] == 0:
            Scount.pop(s[l])
        l+=1
        
        if Scount == Pcount:
            res.append(l)
    return res