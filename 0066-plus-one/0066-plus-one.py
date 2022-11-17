class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i=1        
        while (True):
            if i > len(digits):
                digits.insert(0, 1)
                break
            elif digits[-i] == 9:
                digits[-i] = 0
                i +=1
            else:
                digits[-i] += 1
                break
        return digits
        