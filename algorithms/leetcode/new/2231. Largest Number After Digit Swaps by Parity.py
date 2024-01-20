class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = str(num)
        odds = [x for x in num if int(x) % 2 == 1] 
        evens = [x for x in num if int(x) % 2 == 0] 
        odds.sort()
        evens.sort()
        ans = ''
        for n in num:
            if int(n) % 2 == 1:
                ans += odds.pop()
            else:
                ans += evens.pop()        
        return int(ans)