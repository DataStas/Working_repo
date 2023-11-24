from typing import List


def find_sum(matrix: List[List[int]], x=0, y=0, memo=None) -> int:
    k = str(x) + '_' + str(y)
    if memo is None:
        memo = {}
    if k in memo:
        return memo[k]
    if x >= len(matrix) or y >= len(matrix):
        return 0

    memo[k] = max(find_sum(matrix, x+1, y, memo),
                  find_sum(matrix, x, y+1, memo)) + matrix[x][y]

    return memo[k]



if __name__ == '__main__':
    matrix = [[20, 20, 10, 10],
              [10, 20, 10, 10],
              [10, 20, 20, 20],
              [10, 10, 10, 20]]
    print(find_sum(matrix))