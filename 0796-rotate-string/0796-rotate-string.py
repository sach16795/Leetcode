class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(0, len(s)):
            temp = goal[i:] + goal[:i]
            if temp == s:
                return True
        return False
        
        