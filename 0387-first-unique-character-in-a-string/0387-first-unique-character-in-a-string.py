class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] = -1
            else:
                seen[s[i]] = i
        print(seen)
        ans = -1
        for k,v in seen.items():
            if v == -1:
                continue
            if ans == -1:
                ans = v
            elif v<ans:
                ans = v
        return ans