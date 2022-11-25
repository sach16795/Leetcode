class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        size = len(nums)
        return (size * (size + 1))//2 - sum(nums)