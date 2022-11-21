class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = [0] * 26
        ab = 'abcdefghijklmnopqrstuvwxyz'
        for i in s:
            seen[ab.index(i)] += 1
        for i in s:
            if seen[ab.index(i)] == 1:
                return s.index(i)
        return -1
            
        