class Solution:
    def fib(self, n: int) -> int:
        if n <=1:
            return n
        seen = {0:0,1:1}
        for i in range(2,n+1):
            seen[i] = seen[i-1] + seen[i-2]
        return seen[n]
        # Recursion
        # if n <= 1:
        #     return n
        # else:
        #     return self.fib(n-1) + self.fib(n-2)