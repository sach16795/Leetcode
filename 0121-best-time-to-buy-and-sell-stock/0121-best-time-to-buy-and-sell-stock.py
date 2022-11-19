class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: BruteForce
        profit = 0
        prevmin = prices[0]
        for i in range(0, len(prices)):
            prevmin = prices[i] if prices[i] < prevmin else prevmin
            profit = prices[i] - prevmin if prices[i] - prevmin >= profit else profit
        return profit
        
        
        