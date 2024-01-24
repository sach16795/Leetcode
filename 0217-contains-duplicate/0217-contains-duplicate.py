class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Approach 1
        return len(set(nums)) != len(nums)
        # Approach 2: TLE
        # seen = []
        # for i in nums:
        #     if i in seen:
        #         return True
        #     seen.append(i)
        # return False