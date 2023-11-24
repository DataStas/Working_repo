from typing import List
import random
# Memoized O(n*m^2), O(m^2) n - len(arr) m - target 1 + 1 + 1 wrost case
# Brute O(n^m*m) O(m^2)


def best_sum(target: int, numbers: List[int], memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortest = None
    for n in numbers:
        diff = target - n
        res = best_sum(diff, numbers, memo) 
        if res is not None:
            combination = res + [n]
            if shortest is None or len(combination) < len(shortest):
                shortest = combination

    memo[target] = shortest
    return memo[target]

def test(test_n=10):
    print(best_sum(300, [7, 14]))
    print(best_sum(7, [2, 4]))
    print(best_sum(7, [2, 3]))
    print(best_sum(7, [5, 3, 4, 7]))
    print(best_sum(8, [2, 3, 5]))
    for test in range(test_n):
        n = random.randint(0, 20)
        arr = [random.randint(3, 50) for _ in range(5)]
        print(n, arr, best_sum(n, arr))


if __name__ == "__main__":
    # test(20)