class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # approach 1: Brute Force
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return [i,j]
                
        # approach 2: Memory map
        seen = {}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [i, seen[complement]]
            seen[nums[i]] = i