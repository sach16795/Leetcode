class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        size = len(nums)
        min_seen = 9999999
        if sum(nums) < target:
            return 0
        temp = 0
        
        while i < size and j < size:
            temp += nums[j]
            if temp >= target:
                if min_seen > j-i:
                    min_seen = j-i
                temp -= nums[i]
                temp -= nums[j]
                i = i+1
            else:
                j+=1
        return min_seen +1