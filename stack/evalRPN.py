class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arr = ["+","-","*","/"]

        for char in tokens:
            if char not in arr:
                stack.append(int(char))
            else:
                a = stack.pop()
                b = stack.pop()
               
                if char == "+":
                    c = a + b
                    stack.append(c)
                if char == "-":
                    c = b - a
                    stack.append(c)
                if char == "/":
                    c = int(b / a)
                    stack.append(c)
                if char == "*":
                    c = a * b
                    stack.append(c)
        return stack.pop()