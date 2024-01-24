def twoOutOfThree(nums1, nums2, nums3):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type nums3: List[int]
    :rtype: List[int]
    """
    nums1 = set(nums1)
    nums2 = set(nums2)
    nums3 = set(nums3)
    inter_12 = nums1.intersection(nums2)
    inter_13 = nums1.intersection(nums3)
    inter_32 = nums3.intersection(nums2)
    inter_13.update(inter_32)
    inter_12.update(inter_13)
    return list(inter_12)


if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2,3]
    nums3 = [1, 2]
    print(twoOutOfThree(nums1, nums2, nums3))
