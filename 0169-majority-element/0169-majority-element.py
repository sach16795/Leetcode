class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Appraoch 2: Moores Voting
        mc = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if mc != nums[i]:
                count -= 1
                if count == 0:
                    mc = nums[i]
                    count += 1
            else:
                count += 1
        return mc
        
        
        # Approach 1:
        # vals = {}
        # for i in nums:
        #     if i in vals:
        #         vals[i] = vals[i] + 1
        #     else:
        #         vals[i] = 1
        # for key,value in vals.items():
        #     if value > (len(nums)/2):
        #         return key