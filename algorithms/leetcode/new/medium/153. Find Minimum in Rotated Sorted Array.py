def findMin(nums):
    n = len(nums)
    l = 0
    r = n-1
    smallest = nums[0]

    while (l <= r):
        if nums[r] > nums[l]:
            if nums[l] < smallest:
                smallest = nums[l]
            break

        m = (r+l) / 2
        if nums[m] < smallest:
            smallest = nums[m]

        if nums[m] < nums[l]:
            r = m - 1
        else:
            l = m + 1

    return smallest


if __name__ == "__main__":
    print(findMin([7,1,5,3,6,4]))
#     [0,1,2,4,5,6,7]
    # [7,0,1,2,4,5,6]
    # [6,7,0,1,2,4,5]
    # [5,6,7,0,1,2,4]
    # [4,5,6,7,0,1,2]
    # [2,4,5,6,7,0,1]