class Solution:
    def isValid(self, s: str) -> bool:

        matches = {')' : '(', ']' : '[', '}' : '{'}
        stack = []

        for c in s:
            if c == ')' or c == ']' or c == '}':
                if not stack:
                    return False
                elif stack.pop() != matches[c]:
                    return False
            else:
                stack.append(c)
        
        if not stack:
            return True
        
        return False