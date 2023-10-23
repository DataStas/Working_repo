from typing import List
from functools import reduce


def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid
    left_part = arr[left:left+left_size]
    right_part = arr[mid+1:right_size+1+mid]

    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = left     # Initial index of merged subarray
    while i < left_size and j < right_size:
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    while i < left_size:
        arr[k] = left_part[i]
        i += 1
        k += 1
    while j < right_size:
        arr[k] = right_part[j]
        j += 1
        k += 1


def merge_sort(nums: List[int], left=0, right=0):
    if left < right:

        mid = left + (right-left)//2
        # print(left, right, mid)
        merge_sort(nums, left, mid)
        merge_sort(nums, mid+1, right)
        merge(nums, left, mid, right)


if __name__ == '__main__':
    # print(merge_sort([13, 17, 37, 73, 31, 19, 23]))
    # n = input()
    nums = list(map(int, input().split()))
    # nums = [13, 17, 37, 73, 31, 19, 23]
    merge_sort(nums, 0, len(nums)-1)
    print(*nums)