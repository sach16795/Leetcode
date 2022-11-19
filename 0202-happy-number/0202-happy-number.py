class Solution:
    def isHappy(self, n: int) -> bool:
        seen = []
        seen.append(n)
        while True:
            add = 0 
            for digit in str(n):
                add += int(digit) **2
            if add ==1:
                return True
            elif add in seen:
                return False
            else:
                seen.append(add)
            n = add
                