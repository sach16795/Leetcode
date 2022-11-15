class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lo = 0
        hi = len(nums) -1
        mid = math.ceil((hi-lo)/2)
        
        while(lo <= hi):
            mid = (lo + hi) //2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid -1
            elif target > nums[mid]:
                lo = mid + 1
        return lo 