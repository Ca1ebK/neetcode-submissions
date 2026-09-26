class Solution:
    def calPoints(self, operations: List[str]) -> int:
        '''
        Time: O(n)
        Space: O(n)
        '''
        stack = []
        for op in operations:
            if op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2*stack[-1])
            elif op == '+':
                stack.append(stack[-2] + stack[-1])
            else:
                stack.append(int(op))
        return sum(stack)