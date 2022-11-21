class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Approach 1
        return len(s.strip().split(' ')[-1])