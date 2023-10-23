from typing import List
import random
from functools import reduce


# def merge(nums: List[List[int]]):
#     out = []
#     le = sum(len(n) for n in nums)
#     while le:
#         lowest = []
#         for num in nums:
#             if num:
#                 lowest.append(min(num))
#             else:
#                 lowest.append(10**10)
#         min_ind = lowest.index(min(lowest))
#         try:
#             nums[min_ind].remove(min(lowest))
#         except ValueError:
#             print(min(lowest), nums, min_ind)
#         out.append(min(lowest))
#         le -= 1
#     return out


# def merge_2(arr1: List[int], arr2: List[int]):
#     merged = []
#     while arr1 or arr2:
#         if arr2:
#             m2 = min(arr2)
#         else:
#             m2 = 10**10
#         if arr1:
#             m1 = min(arr1)
#         else:
#             m1 = 10**10
#         if m1 > m2:
#             merged.append(m2)
#             arr2.remove(m2)
#         else:
#             merged.append(m1)
#             arr1.remove(m1)
#     return merged

def merge_2(arr1: List[int], arr2: List[int]):
    merged = []
    while arr1 or arr2:
        if arr1 and arr2:
            if arr1[0] > arr2[0]:
                merged.append(arr2[0])
                arr2.remove(arr2[0])
            else:
                merged.append(arr1[0])
                arr1.remove(arr1[0])
        elif arr2:
            merged.append(arr2[0])
            arr2.remove(arr2[0])
        else:
            merged.append(arr1[0])
            arr1.remove(arr1[0])

    return merged


def merge(nums: List[List[int]]):
    out = reduce(merge_2, nums)
    return out


def test_sort(n):
    nums = [[random.randint(0, 1000) for _ in range(n)] for _ in range(5)]
    # print(merge(nu))
    return merge(nums=nums)


if __name__ == "__main__":
    # n = input()
    # nums = [int(x) for x in input().split()]
    # nums = (map(int, input().split()))
    # n = int(input())
    # nums = [list(map(int, input().split())) for _ in range(n*2)]
    # nums = [x for ind, x in enumerate(nums) if ind % 2 == 1]
    # print(nums)
    print(test_sort(7))