class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0
        for i in words:
            ans = ans + 1 if i.startswith(pref) else ans
        return ans