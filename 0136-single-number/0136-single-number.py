class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        vals = []
        for num in nums:
            if num in vals:
                vals.remove(num)
            else:
                vals.append(num)
        return vals[0]