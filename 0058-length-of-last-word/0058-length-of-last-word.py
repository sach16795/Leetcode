class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.strip().split(" ")) ==1:
            return len(s.strip())
        else:
            return len(s.strip().split(" ")[-1])
        