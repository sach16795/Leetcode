class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        temp = []
        temp.extend(nums)
        temp.extend(nums)
        return temp