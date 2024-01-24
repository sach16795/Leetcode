class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            if i in seen:
                seen[i] = seen[i] +1
            else:
                seen[i] = 1
        top = sorted(seen.values(),reverse=True)[0:k]
        ans = []
        for key,val in seen.items():
            if val in top:
                ans.append(key)
        return ans