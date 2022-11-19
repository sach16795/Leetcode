class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1last = None
        word2last = None
        minDist = len(wordsDict)
        for i in range(0, len(wordsDict)):
            if wordsDict[i] == word1:
                word1last = i
            elif wordsDict[i] == word2:
                word2last = i
            if word1last is not None and word2last is not None:
                minDist = abs(word2last - word1last) if abs(word2last - word1last) < minDist else minDist
        return minDist