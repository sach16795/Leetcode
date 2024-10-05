class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen1 = {}
        seen2 = {}
        if len(s2) < len(s1):
            return False
        for i in s1:
            seen1[i] = seen1[i] + 1 if i in seen1 else 1

        for i in range(len(s1)):
            seen2[s2[i]] = seen2[s2[i]] + 1 if s2[i] in seen2 else 1
            
        i = 0
        while i + len(s1) <= len(s2):
            boo = True
            for j in seen1:
                if j not in seen2 or seen1[j] != seen2[j]:
                    boo = False
                    break
            if boo:
                return True
            seen2[s2[i]] -= 1
            if i + len(s1) < len(s2):
                seen2[s2[i+ len(s1)]] = seen2[s2[i+ len(s1)]] + 1 if s2[i+ len(s1)] in seen2 else 1
            i +=1
            

        return False

            
                