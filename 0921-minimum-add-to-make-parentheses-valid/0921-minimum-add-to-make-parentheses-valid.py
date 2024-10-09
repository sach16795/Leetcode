class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        seen = []
        ans = 0
        for i in s:
            if i == "(":
                seen.append(i)
            elif i == ")" and len(seen) > 0:
                seen.pop()
            else:
                ans += 1
        return len(seen) + ans