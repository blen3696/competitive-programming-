'''844. Backspace String Compare

Given two strings s and t, return true if they are equal when both are typed 
into empty text editors.
'#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".'''
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1  = []
        stack2 = []

        for char in s:
            if char =="#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(char)
        for char in t:
            if  char =="#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(char)
        if stack1 == stack2:
            return True
        return False
            
