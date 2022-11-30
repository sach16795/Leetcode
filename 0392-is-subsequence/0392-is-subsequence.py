class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if (len(s) == 0 and len(t) == 0) or (len(s) == 0):
            return True
        elif len(t) == 0:
            return False
        
        s = list(s)
        current = s.pop(0)
        for i in t:
            if i == current:
                if len(s) == 0:
                    return True
                current = s.pop(0)
        return False
                
        
        