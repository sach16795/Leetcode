class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        lmax = 0
        rmax = 0
        ans = 0

        while l < r:
            lmax = lmax if lmax > height[l] else height[l]
            rmax = rmax if rmax > height[r] else height[r]
            if lmax < rmax:
                if min(height[l],rmax) * (r-l) > ans:
                    ans = min(height[l],rmax) * (r-l)
                l+=1
            else:
                if min(height[r],lmax) * (r-l) > ans:
                    ans = min(height[r],lmax) * (r-l)
                r-=1
        return ans