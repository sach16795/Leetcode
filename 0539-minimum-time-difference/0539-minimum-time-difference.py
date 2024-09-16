class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        seen = []
        for i in timePoints:
            seen.append(int(i.split(":")[0])*60 + int(i.split(":")[1]))
            seen.append(1440 + (int(i.split(":")[0])*60 + int(i.split(":")[1])))
        seen = sorted(seen)
        ans = 1440
        for i in range(1, len(seen)):
            ans = seen[i] - seen[i-1] if ans > seen[i] - seen[i-1] else ans
        return ans