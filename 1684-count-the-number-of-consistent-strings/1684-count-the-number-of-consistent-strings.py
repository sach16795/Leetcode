class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            flag = True
            for i in word:
                if i not in allowed:
                    flag = False
                    continue
            ans = ans + 1 if flag else ans
        return ans