class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        
        if "e" in s:
            if s.count("e") > 1:
                return False
            try:
                base = float(s.split("e")[0])
                exp = int(s.split("e")[1])
                return True
            except:
                return False
        else:
            try:    
                test = float(s)
                return s.lower() == s.upper()
            except:
                return False
            
            