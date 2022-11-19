class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        # Apporach 1 
        count = 100000
        for i in target:
            count = s.count(i)//target.count(i) if  s.count(i)//target.count(i) < count else count
        return count
        