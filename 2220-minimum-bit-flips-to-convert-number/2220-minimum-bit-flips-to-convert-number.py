class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        
        diff = abs(len(start) - len(goal))
        start = ('0' * diff) + start if len(start) < len(goal) else start
        goal = ('0' * diff) + goal if len(goal) < len(start) else goal

        ans = 0
        for i in range(len(start)):
            if start[i] == goal[i]:
                continue
            ans +=1
        return ans