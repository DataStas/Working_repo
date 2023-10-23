from typing import List
import random


def select_sort(nums: List):
    l = 0
    while l < len(nums):
        re = nums.index(min(nums[l:]))
        nums[l], nums[re] = nums[re], nums[l]
        l += 1
    return nums


def test_sort(n):
    nums = [random.randint(0, 1000) for _ in range(n)]
    return select_sort(nums=nums)


if __name__ == "__main__":
    # n = input()
    # nums = [int(x) for x in input().split()]
    nums = list(map(int, input().split()))
    print(nums)
    print(test_sort(7))