class Solution:
    def minimumChairs(self, s: str) -> int:
        ans = 0
        curr = 0
        for i in s:
            if i =="E":
                curr += 1 
            elif i =="L":
                curr -= 1 
            if curr > ans:
                ans=curr
        return ans