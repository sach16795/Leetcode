class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Approach 1:
        vals = {}
        for i in nums:
            if i in vals:
                vals[i] = vals[i] + 1
            else:
                vals[i] = 1
        for key,value in vals.items():
            if value > (len(nums)/2):
                return key