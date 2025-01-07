class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s = s.split(" ")
        ans = ""
        for i in s[::-1]:
            if i != "":
                ans += i
                ans += " "
        return ans.strip()