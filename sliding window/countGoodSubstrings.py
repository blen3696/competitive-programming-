'''1876. Substrings of Size Three with Distinct Characters

A string is good if there are no repeated characters.

Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.

Note that if there are multiple occurrences of the same substring, every occurrence should be counted.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "xyzzaz"
Output: 1
Explanation: There are 4 substrings of size 3: "xyz", "yzz", "zza", and "zaz". 
The only good substring of length 3 is "xyz".
Example 2:

Input: s = "aababcabc"
Output: 4
Explanation: There are 7 substrings of size 3: "aab", "aba", "bab", "abc", "bca", "cab", and "abc".
The good substrings are "abc", "bca", "cab", and "abc".
 

Constraints:

1 <= s.length <= 100
s​​​​​​ consists of lowercase English letters.'''
class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        Scount = {}
        good_sub = 0
        if len(s) < 3:
            return 0
        for i in range(3):
            Scount[s[i]] = 1 + Scount.get(s[i],0)
        if all(count == 1 for count in Scount.values()):
             good_sub +=1
        for r in range(3, len(s)):
             Scount[s[r]] = 1 + Scount.get(s[r],0)
             Scount[s[l]] -=1
             if Scount[s[l]] == 0:
                 Scount.pop(s[l])
             l+=1
             if all(count == 1 for count in Scount.values()):
                 good_sub +=1
        return good_sub

