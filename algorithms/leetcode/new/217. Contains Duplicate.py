def containsDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # return False if len(set(nums)) == len(nums) else True
    d = {}
    for n in nums:
        if n in d:
            return True
        else:
            d[n] = 0
    return False


if __name__ == "__main__":
    print(containsDuplicate([1, 2, 3, 1]))