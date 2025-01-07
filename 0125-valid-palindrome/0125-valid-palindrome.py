class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        lo = 0
        hi = len(s) - 1
        while (lo < hi):
            if not(s[lo].isalnum()) :
                lo +=1
                continue
            elif not(s[hi].isalnum()) :
                hi -=1
                continue
            else:
                if s[lo] != s[hi]:
                    return False
                lo += 1
                hi -= 1
        return True        