class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        vals = {}
        for idx in range (0,len(nums)):
            if nums[idx] in vals:
                if abs(vals[nums[idx]] - idx) <= k:
                    return True
                else:
                    vals[nums[idx]] = idx
            else:
                vals[nums[idx]] = idx
        return False