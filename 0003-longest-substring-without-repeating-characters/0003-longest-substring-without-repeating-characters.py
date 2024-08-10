class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = ""
        for i in range(len(s)):
            seen = set()
            seen.add(s[i])
            curr = s[i]
            for j in range(i+1,len(s)):
                if s[j] in seen:
                    break
                curr += s[j] 
                seen.add(s[j])
            ans = ans if len(ans) > len(curr) else curr
        return len(ans)