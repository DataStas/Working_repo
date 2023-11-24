from typing import List
import random
# O(n*m), O(m) n - len(arr) m - target 1 + 1 + 1 wrost case
# Brute O(n^m)


def target_sum(target: int, numbers: List[int], memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return True
    if target < 0:
        return False
    for n in numbers:
        diff = target - n
        if target_sum(diff, numbers, memo):
            memo[target] = True  # not important
            return True

    memo[target] = False  # not important
    return False


def test(test_n=10):
    print(target_sum(300, [7, 14]))
    print(target_sum(7, [2, 4]))
    print(target_sum(7, [2, 3]))
    print(target_sum(7, [5, 3, 4, 7]))
    print(target_sum(8, [2, 3, 5]))

    for test in range(test_n):
        n = random.randint(1, 20)
        arr = [random.randint(3, 50) for _ in range(5)]
        print(n, arr, target_sum(n, arr))


if __name__ == "__main__":
    test(20)