from typing import List
import random
# O(n*m^2), O(m^2) n - len(arr) m - target 1 + 1 + 1 wrost case
# Brute O(n^m*m) O(m)


def how_sum(target: int, numbers: List[int], memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    for n in numbers:
        diff = target - n
        res = how_sum(diff, numbers, memo) 
        if res is not None:
            memo[target] = res + [n]
            return memo[target]

    memo[target] = None
    return memo[target]

def test(test_n=10):
    print(how_sum(300, [7, 14]))
    print(how_sum(7, [2, 4]))
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(8, [2, 3, 5]))
    for test in range(test_n):
        n = random.randint(0, 20)
        arr = [random.randint(3, 50) for _ in range(5)]
        print(n, arr, how_sum(n, arr))


if __name__ == "__main__":
    test(20)