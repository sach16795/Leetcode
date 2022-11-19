class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Approach 1. 
        one = max(nums)
        nums.remove(one)
        two = max(nums)
        return (one-1)*(two -1)