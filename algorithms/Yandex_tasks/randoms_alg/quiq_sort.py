from typing import List, Callable
import random


def quicksort(arr, start, stop):
    if (start < stop):
        pivotindex = partitionrand(arr, start, stop)
        quicksort(arr, start, pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)


def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = arr[randpivot], arr[start]
    return partition(arr, start, stop)


def partition(arr, start, stop):
    pivot = start
    i = start + 1
    for j in range(start + 1, stop + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] = arr[i - 1], arr[pivot]
    pivot = i - 1
    return (pivot)


def test(fun: Callable):
    # arr = [random.randint(1, 10) for _ in range(10)]
    arr = [4, 7, 2, 5, 3, 1, 8, 9, 6]
    fun(arr, 0, len(arr)-1)
    print(arr)


if __name__ == "__main__":
    test(quicksort)