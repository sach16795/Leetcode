class Solution:
    def isValid(self, s: str) -> bool:
        opp = {')': '(',
           '}': '{',
           ']': '['}
        stack = []
        for char in s:
            if len(stack) != 0 and stack[-1] == opp.get(char):
                stack.pop()
            else:
                stack.append(char)
        return len(stack) == 0 
                    
        