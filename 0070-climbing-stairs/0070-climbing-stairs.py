class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        seen = {1:1,2:2}
        for i in range(3,n+1):
            seen[i] = seen[i-1] + seen[i-2]
        return seen[n]