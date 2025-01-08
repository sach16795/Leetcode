class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        lo = 0
        hi = len(s) - 1

        while(lo < hi):
            if s[lo] == s[hi]:
                lo+=1
                hi-=1
                continue
            else:
                if s[lo:hi] == s[lo:hi][::-1] or s[lo+1:hi+1] == s[lo+1:hi+1][::-1]:
                    return True
                else:
                    return False

        return True