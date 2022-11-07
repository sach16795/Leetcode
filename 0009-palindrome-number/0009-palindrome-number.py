import math
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Approach 1
        # if len(str(x)) <= 1:
        #     return True
        # strx = str(x)
        # for i in range (0, ceil((len(strx)-1)/2)):
        #     if strx[i] == strx[len(strx) - i - 1]:
        #         continue
        #     else:
        #         return False
        # return True
        
        # Approach 2
        return str(x)[::-1] == str(x)