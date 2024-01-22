class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_final = []
        t_final = []
        
        for i in range(max(len(s), len(t))):
            if i < len(s):
                if s[i] == "#":
                    if len(s_final) > 0:
                        s_final.pop()
                else:
                    s_final.append(s[i])
            if i < len(t):
                if t[i] == "#":
                    if len(t_final) > 0:
                        t_final.pop()
                else:
                    t_final.append(t[i])
        print(s_final)
        print(t_final)
        return s_final == t_final