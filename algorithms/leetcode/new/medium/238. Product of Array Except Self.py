def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    length = len(nums)
    products = [1] * len(nums)
    for i in range(1, length):
        products[i] = products[i-1] * nums[i-1]  

    right = nums[-1]
    for i in range(length-2, -1, -1): # -1 couse range [len-2, len-3, len-4 ... 0 -1)
        products[i] *= right
        right *= nums[i]

    return products


if __name__ == '__main__':
    print(productExceptSelf([1, 2, 3, 4]))