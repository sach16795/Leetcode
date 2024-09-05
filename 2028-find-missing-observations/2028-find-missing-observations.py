class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        
        total = (n+m) * mean
        diff = total -sum(rolls)
        
        if diff < n or diff > 6*n:
            return []
        ans = [1] * n
        diff -= n
        i = 0
        while diff>0:
            if ans[i] ==6:
                i+=1
                continue
            ans[i] +=1
            diff -=1
        return ans