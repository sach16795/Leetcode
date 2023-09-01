class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Approach 1: Two pointer. Timed out.
        # profit = 0
        # for i in range(0,len(prices)):
        #     for j in range (i+1, len(prices)):
        #         if prices[j] - prices[i] > profit:
        #             profit =  prices[j] - prices[i]
        # return profit
        # Approach 2
        minseen = 100000
        profit = 0 
        for i in range(0, len(prices)):
            if prices[i] < minseen:
                minseen = prices[i]
            if prices[i] - minseen > profit:
                profit = prices[i] - minseen
        return profit
                