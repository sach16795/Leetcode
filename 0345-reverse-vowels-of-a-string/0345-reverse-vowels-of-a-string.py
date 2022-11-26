class Solution:
    def reverseVowels(self, s: str) -> str:
        lo = 0
        hi = len(s)-1
        v = ['a','e','i','o','u', 'A', 'E', 'I', 'O', 'U']
        s = list(s)
        while lo < hi:
            if s[lo] in v and s[hi] in v:
                temp = s[hi]
                s[hi] = s[lo]
                s[lo] = temp
                hi -= 1
                lo += 1
                continue
            if s[hi] not in v:
                hi -=1
            if s[lo] not in v:
                lo +=1
        return ''.join([i for i in s])