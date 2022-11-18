class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Approach 3:
        vals = {}
        for num in nums:
            if num in vals:
                vals.pop(num)
            else:
                vals[num] = 1
        return list(vals.keys())[0]
        
        # Approach 2: Naive iteration
        # for num in nums:
        #     if nums.count(num) == 1:
        #         return num
        
        # Approach 1: Naive iteration with list
        # vals = []
        # for num in nums:
        #     if num in vals:
        #         vals.remove(num)
        #     else:
        #         vals.append(num)
        # return vals[0]