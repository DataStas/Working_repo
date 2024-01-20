class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        r = len(num)-1
        while r >= 0:
            if int(num[r]) % 2 == 1:
                return num[:r+1]
            r -= 1
        return ""