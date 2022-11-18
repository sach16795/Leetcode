class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num
        # Approach 1: Naive iteration
        # vals = []
        # for num in nums:
        #     if num in vals:
        #         vals.remove(num)
        #     else:
        #         vals.append(num)
        # return vals[0]