class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Approach 1 2-pointer
        insert = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[insert] = nums[i]
                insert +=1
        return insert
                
                
        