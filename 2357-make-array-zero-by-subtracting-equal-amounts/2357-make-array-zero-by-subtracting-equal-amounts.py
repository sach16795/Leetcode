class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        count = 0
        while nums.count(0) != len(nums):
            count +=1
            n = min([value for value in nums if value!=0])
            for i in range(0,len(nums)):
                if nums[i] !=0:
                    nums[i] = nums[i] - n
        return count
        
        