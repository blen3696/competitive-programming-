'''20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input
string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 '''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        my_dic = {"(": ")", "[": "]", "{": "}"}
        stack =[]
        for char in s:
            if char in my_dic.keys():
                stack.append(char)
            else:
                if not stack:
                    return False
                a = stack.pop()
                if my_dic[a] != char:
                    return False
        return not stack