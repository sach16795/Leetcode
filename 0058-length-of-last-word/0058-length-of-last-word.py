class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip()) if len(s.strip().split(" ")) == 1 else len(s.strip().split(" ")[-1])
        