class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        seen = {}
        ans = []
        for i in intervals:
            seen[i[0]] = i[1] if i[0] not in seen else max(i[1], seen[i[0]])
        srt = sorted(seen.keys())
        last = None
        for i in srt:
            if last is None:
                last = [i, seen[i]]
                continue
            if i > last[0] and seen[i] < last[1]:
                continue
            if i <= last[1] and seen[i] >= last[1]:
                last = [last[0], seen[i]]
            else:
                ans.append(last)
                last = [i,seen[i]]
        if last is not None:
            ans.append(last)
        return ans
            
