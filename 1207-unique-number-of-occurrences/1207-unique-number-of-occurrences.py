class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        vals = set(arr)
        for i in vals:
            if arr.count(i) in seen:
                return False
            else:
                seen.add(arr.count(i))
        return True