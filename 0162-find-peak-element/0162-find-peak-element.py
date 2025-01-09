class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)< 2:
            return 0
        for i in range(0, len(nums)):
            if (i == 0 and nums[0] > nums[1]) or (i == len(nums)-1 and nums[len(nums)-1] > nums[len(nums) -2]):
                return i
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i