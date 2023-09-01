class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #Approach 1: use sorted
        if sorted(nums) == nums or sorted(nums,reverse=True) == nums:
            return True
        else:
            print(nums.sort())
            return False
        # Approach 2: O(n)
        if len(nums) == 1 or (nums[0] - nums[-1] == 0): 
            return True
        elif (nums[0] - nums[-1] < 0):
            for i in range(0, len(nums)):
                if nums[i + 1] - nums[i] < 0:
                    return False
        elif (nums[0] - nums[-1] > 0):
            for i in range(0, len(nums)):
                if nums[i + 1] - nums[i] > 0:
                    return False
        return True