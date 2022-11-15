class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insert = 0
        current = 0
        while current < len(nums):
            prevval = nums[current]
            while (current +1 < len(nums) and nums[current+1] == prevval):
                current += 1
            nums[insert] = prevval
            insert+=1
            current +=1
        return insert
            
        