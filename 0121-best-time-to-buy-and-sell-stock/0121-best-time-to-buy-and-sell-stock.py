class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprof = 0
        currmin = 1000000000
        
        for i in prices:
            if i < currmin:
                currmin = i
            if maxprof < i - currmin:
                maxprof = i - currmin
        return maxprof