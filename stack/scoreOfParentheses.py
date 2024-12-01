class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        
        for char in s:
            if char == "(":
                stack.append(0)
            else:
                a = stack.pop()
                if a == 0:
                   stack[-1] += 1
                else:
                    stack[-1] += a*2
        return stack[0]
    