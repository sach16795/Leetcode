class Solution:
    def isValid(self, s: str) -> bool:
        # Approach 1
        opp = {')': '(',
           '}': '{',
           ']': '['}
        
        stack = []
        for char in s:
            if len(stack) != 0 and stack[-1] == opp.get(char):
                stack.pop()
            elif char in opp.keys():
                return False
            else:
                stack.append(char)
        return len(stack) == 0 
                    
        