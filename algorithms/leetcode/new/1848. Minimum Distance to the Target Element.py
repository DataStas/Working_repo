def getMinDistance(nums, target, start):
    """
    :type nums: List[int]
    :type target: int
    :type start: int
    :rtype: int
    """
    d = {}
    for ind, n in enumerate(nums):
        if n == target:
            if n in d:
                d[target] = min(d[n], abs(ind-start))
            else:
                d[target] = abs(ind-start)
    return d[target]


if __name__ == "__main__":
    print(getMinDistance([5, 3, 6], 5, 2))
