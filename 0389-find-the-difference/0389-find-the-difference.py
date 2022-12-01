class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Approach 2: 2 maps
        sseen = {}
        tseen = {t[-1]:1}
        for i in range(0,len(s)):
            sseen[s[i]] = sseen[s[i]] + 1 if s[i] in sseen else 1
            tseen[t[i]] = tseen[t[i]] + 1 if t[i] in tseen else 1
        for key, val in tseen.items():
            if key not in sseen or val != sseen[key]:
                return key
        
            
        # Approach 1: Sort and 2 pointed
        # s = sorted(s)
        # t = sorted(t)
        # for i in range(0, len(s)):
        #     if s[i] != t[i]:
        #         return t[i]
        # return t[-1]