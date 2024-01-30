class Solution:
    def maxArea(self, height: List[int]) -> int:
        imax = 0
        
        i = 0
        j = len(height) - 1
        while j > i:
            cmax = min(height[i],height[j]) * (j-i)
            if cmax > imax:
                imax = cmax
            if height[j] >= height[i]:
                i +=1
            else:
                j-=1
        return imax
                    