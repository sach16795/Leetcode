class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) ==0:
            return 0
        s = sorted(nums)
        curr = 1
        res = 1
        
        for i in range(0,len(nums)-1):
            if s[i+1] != s[i]:
                if s[i+1] - s[i] == 1:
                    curr +=1
                    res = curr if res < curr else res
                else:
                    curr = 1
                    res = curr if res < curr else res
        return res
            