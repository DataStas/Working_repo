def maxAscendingSum(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        prev = nums[0]
        cur = nums[0]
        for i in range(1, len(nums)):
            if prev >= nums[i]:
                ans = max(cur, ans)
                cur = nums[i]
            else:
                cur += nums[i]
            prev = nums[i]
        return max(cur, ans)

if __name__ == "__main__":
    print(maxAscendingSum([12,17,15,13,10,11,12]))