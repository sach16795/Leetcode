class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map solution || Order N.
        seen = {}
        for idx, num in enumerate(nums):
            if target-num in seen:
                return [idx, seen[target-num]]
            else:
                seen[num] = idx