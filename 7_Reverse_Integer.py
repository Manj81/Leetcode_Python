class Solution:
    def reverse(self, x: int) -> int:
        isNegative = False
        if x < 0:
            isNegative = True
            x = -x
        
        reverse = 0
        while x != 0:
            remainder = x%10
            reverse = (reverse * 10) + remainder
            x = x //10
        if x <= -2 **31 and x >= 2 **31 - 1:
            return 0
        return -reverse if isNegative else reverse