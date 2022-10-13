class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution || Order N.
        for idx in range (0, len(nums)):
            for jdx in range(idx+1, len(nums)):
                if nums[idx] + nums[jdx] == target:
                    return [idx,jdx]