class Solution:
    def isPalindrome(self, s: str) -> bool:
        ab = "abcdefghijklmnopqrstuvwxyz0123456789"
        clean = ''
        for i in s:
            if i.lower() in ab:
                clean += i.lower()
        print(clean)
        return clean == clean[::-1]