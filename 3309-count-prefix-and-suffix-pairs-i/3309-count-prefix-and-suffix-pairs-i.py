class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0
        if len(words) <= 1:
            return ans
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                ans = ans + 1 if self.isPrefixAndSuffix(words[i], words[j]) else ans
        return ans

    def isPrefixAndSuffix(self,str1, str2):
        return str2.startswith(str1) and str2.endswith(str1)