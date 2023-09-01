class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Approach 1: use sorted
        if sorted(nums) == nums or sorted(nums,reverse=True) == nums:
            return True
        else:
            print(nums.sort())
            return False
        