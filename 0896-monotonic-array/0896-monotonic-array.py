class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Approach 1: use sorted
        # if sorted(nums) == nums or sorted(nums,reverse=True) == nums:
        #     return True
        # else:
        #     print(nums.sort())
        #     return False
        # Approach 2
        increasing = decreasing = True
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                decreasing = False
            elif nums[i] < nums[i-1]:
                increasing = False
                
        return increasing or decreasing