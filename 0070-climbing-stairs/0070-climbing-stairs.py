class Solution:
    vals = {1:1,
           2:2}
    def climbStairs(self, n: int) -> int:
        count = 0
        if n == 1:
            return self.vals[1]
        if n == 2:
            return self.vals[2]
        elif n >= 3:
            n_1 = self.climbStairs(n-1)
            if n-1 not in self.vals:
                self.vals[n-1] = n_1
        return self.vals[n-1] + self.vals[n-2]