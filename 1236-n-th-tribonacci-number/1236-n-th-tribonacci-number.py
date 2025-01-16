class Solution:
    def tribonacci(self, n: int) -> int:
        if n ==0 :
            return 0
        elif n ==1 or n == 2:
            return 1
        seen = {0:0,1:1,2:1}
        for i in range(3,n+1):
            seen[i] = seen[i-1] + seen[i-2] + seen[i-3]
        return seen[n]
        # Recursion: TLE
        # if n ==0 :
        #     return 0
        # elif n ==1 or n == 2:
        #     return 1
        # else:
        #     return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3) 