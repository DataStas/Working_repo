def answerQueries(nums, queries):
    """
    :type nums: List[int]
    :type queries: List[int]
    :rtype: List[int]
    """
    nums.sort()
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    ans = []
    for q in queries:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > q:
                r = m - 1
            else:
                l = m + 1
        ans.append(l)
    return ans            

if __name__ == "__main__":
    print(answerQueries([736411,184882,914641,37925,214915], [331244,273144,118983,118252,305688,718089,665450]))