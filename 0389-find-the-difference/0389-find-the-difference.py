class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Approach 1: Sort and 2 pointed
        s = sorted(s)
        t = sorted(t)
        for i in range(0, len(s)):
            if s[i] != t[i]:
                return t[i]
        return t[-1]