class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        if len(words) == 1:
            return list(ans)
        for i in range(0, len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.add(words[i])
                if words[j] in words[i]:
                    ans.add(words[j])
        return list(ans)
                    
                    