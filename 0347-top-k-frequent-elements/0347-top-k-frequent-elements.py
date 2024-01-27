class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) +1
        top = sorted(seen.values(),reverse=True)[0:k]
        ans = []
        for key,val in seen.items():
            if val in top:
                ans.append(key)
        return ans