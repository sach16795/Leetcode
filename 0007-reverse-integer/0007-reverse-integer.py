class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        a = int(str(a)[::-1])
        a = a if x > 0 else (a*(-1))
        return a if (a > -2 **31) and a <= (2 **31)-1 else 0
        