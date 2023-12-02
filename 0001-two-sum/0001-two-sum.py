class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
         # approach 1: Brute Force
        # for i in range(0, len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j] == target):
        #             return [i,j]
        #
        # approach 2: Memory map
        # Map solution || Order N.
        seen = {}
        for idx, num in enumerate(nums):
            if target-num in seen:
                return [idx, seen[target-num]]
            else:
                seen[num] = idx