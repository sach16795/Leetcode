class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        ans = [0] * len(boxes)
        for i in range(0,len(boxes)):
            if boxes[i] =="1":
                for j in range(0,len(boxes)):
                    if i == j:
                        continue
                    ans[j] += abs(j-i)
        return ans