from typing import List


# def find_sum_util(matrix, i, j):
#     global dp 
#     if (i == 0 or j == 0):
#         return 0
#     if (dp[i][j] != -1):
#         return dp[i][j]
#     dp[i][j] = max(find_sum_util(matrix, i, j-1), find_sum_util(matrix, i-1, j)) + matrix[i-1][j-1]
#     print(dp)
#     return dp[i][j]


# def find_sum(matrix):
#     global dp
#     n = len(matrix)
#     m = len(matrix[0])
#     dp = [[-1 for i in range(m + 1)] for j in range(n + 1)]
#     return find_sum_util(matrix, n, m)


# def find_sum(m):
#     p = [0] * (len(m) + 1)
#     for l in m:
#         for i, v in enumerate(l, 1):
#             p[i] = v + max(p[i-1], p[i])
#     return p[-1]

def find_sum(m):
    global cache
    cache = [[None] * len(m) for _ in range(len(m[0]))]
    return biggest_sum(m, 0, 0)


def biggest_sum(m, row, col):
    global cache
    if row >= len(m) or col >= len(m[row]):
        return 0
    if cache[row][col] is not None:
        return cache[row][col]
    cache[row][col] = max(m[row][col] + biggest_sum(m, row+1, col), 
                          m[row][col] + biggest_sum(m, row, col+1))
    return cache[row][col]




if __name__ == '__main__':
    matrix = [[20, 20, 10, 10],
              [10, 20, 10, 10],
              [10, 20, 20, 20],
              [10, 10, 10, 20]]
    print(find_sum(matrix))