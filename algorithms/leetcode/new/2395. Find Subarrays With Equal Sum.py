class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        prev = nums[0]
        for i in range(1, len(nums)):
            s = prev + nums[i]
            if s in d:
                return True
            else:
                d[s] = 1
            prev = nums[i]
        return False
        