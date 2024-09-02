class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        for i in range(1,n):
            chalk[i] = chalk[i] + chalk[i-1]
            
        total = chalk[-1]
        rem = k % total
        for i in range(n):
            if chalk[i] > rem:
                return i