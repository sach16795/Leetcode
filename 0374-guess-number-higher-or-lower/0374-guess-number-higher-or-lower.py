# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 0 
        hi = n
        while True:
            mid = (lo + hi) // 2
            result = guess(mid)
            if result == 0:
                break
            elif result ==1:
                lo = mid+1
            elif result == -1:
                hi = mid-1
        return mid
            
            
            
        