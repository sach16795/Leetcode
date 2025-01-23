class Solution:
    def maximumSwap(self, num: int) -> int:
        sort = sorted(str(num), reverse=True)
        s = str(num)
        for i in range(len(s)):
            if s[i] == sort[i]:
                continue
            else:
                temp = s[i]
                s = s.replace(s[i],sort[i],1)
                s = s[::-1].replace(sort[i],temp,1)[::-1]
                return int(s)
        return int(s)