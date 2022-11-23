class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        for i in range(0, len(haystack)):
            if needle[0] == haystack[i] and needle == haystack [i: i+len(needle)]:
                return i