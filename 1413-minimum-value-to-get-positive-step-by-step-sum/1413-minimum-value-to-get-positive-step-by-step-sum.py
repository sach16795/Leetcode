class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        curr_min = 1
        curr_sum = 0
        for i in nums:
            curr_sum += i
            if curr_sum < 1 and curr_sum <= curr_min:
                curr_min = curr_sum -1
        return abs (curr_min) 
        