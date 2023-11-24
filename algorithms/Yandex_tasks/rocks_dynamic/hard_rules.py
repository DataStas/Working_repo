import random
from typing import Tuple


def rocks(n: int, m: int) -> str:
    ans = [[x for x in range(m+1)] for _ in range(n+1)]
    ans[0][0] = 'Loose'
    for i in range(n+1):
        if i % 3 == 0:
            ans[i][0] == 'Loose'
        else:
            ans[i][0] == 'Win'
    for i in range(m+1):
        if i % 3 == 0:
            ans[0][i] == 'Loose'
        else:
            ans[0][i] == 'Win'
    for ind in range(n+1):
        for ind_2 in range(m+1):
            cond_1 = ans[ind][ind_2-1] == 'Win'
            cond_2 = ans[ind-1][ind_2] == 'Win'
            cond_3 = ans[ind-2][ind_2-1] == 'Win'
            cond_4 = ans[ind-1][ind_2-2] == 'Win'
            cond_5 = ans[ind-2][ind_2] == 'Win'
            cond_6 = ans[ind][ind_2-2] == 'Win'
            if all([cond_1, cond_2, cond_3, cond_4, cond_5, cond_6]):
                ans[ind][ind_2] = 'Loose'
            else:
                ans[ind][ind_2] = 'Win'
    return ans[n-1][m-1]


def test(num, bounds: list[int]):
    intervals = []
    for _ in range(num):
        c1 = [random.randint(bounds[0], bounds[1]) for _ in range(2)]
        if c1[0] > c1[1]:
            c1[0], c1[1] = c1[1], c1[0]
        intervals.append(tuple(c1))
    print(intervals)
    return intervals


if __name__ == '__main__':
    n, m = tuple(map(int, input().split()))
    print(rocks(n, m))
    # for _ in range(100):
    #     print(intersec(test(3, (1, 5, 10))))