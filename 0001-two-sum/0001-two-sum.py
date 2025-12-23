class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for idx, value in enumerate(nums):
            if target-value in seen:
                return [idx, seen[target-value]]
            else:
                seen[value] = idx