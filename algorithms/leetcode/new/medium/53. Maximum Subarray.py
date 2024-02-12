from functools import cache
from math import inf

# dynamic recursion
# def maxSubArray(nums):
#     @cache
#     def solve(i, must_pick):
#         if i >= len(nums): return 0 if must_pick else -inf
#         return max(nums[i] + solve(i+1, True), 0 if must_pick else solve(i+1, False))
#     return solve(0, False)


# dynamic tabulation
# def maxSubArray(nums):
#     dp = [[0]*len(nums) for i in range(2)]
#     dp[0][0], dp[1][0] = nums[0], nums[0]
#     for i in range(1, len(nums)):
#         dp[1][i] = max(nums[i], nums[i] + dp[1][i-1]) # у нас есть 2 варианта или шаг вперед или сумма нескольких. Мы выбираем максимальное
#         dp[0][i] = max(dp[0][i-1], dp[1][i]) # Каждое решение из предыдущего шага сравниваем с прошлым решением шаг назад. Выбираем максимальное
#     return dp[0][-1]

# divide and Conquer делим массив на подмассивы и ищем максимальный в лоб. Делим относительно среднего!
def maxSubArray(nums):
    def solve(arr, l, r):
        if l > r: return -10**10
        m, left_s, right_s, cur_s = (l+r) // 2, 0, 0, 0
        for i in range(m-1, l-1, -1):
            left_s = max(left_s, cur_s := cur_s + arr[i])
        cur_s = 0
        for i in range(m+1, r+1):
            right_s = max(right_s, cur_s := cur_s + arr[i])
        return max(solve(arr, l, m-1), solve(arr, m+1, r), left_s+right_s+arr[m])
    return solve(nums, 0, len(nums)-1)



"""We can further optimize the previous solution. 
    The O(N) term in the recurrence relation of previous solution was due to 
    computation of max sum subarray involving nums[mid] in each recursion.
    
    But we can reduce that term to O(1) if we precompute it.
    This can be done by precomputing two arrays pre and suf where pre[i] will denote maximum sum subarray ending at i
    and suf[i] denotes the maximum subarray starting at i.
    pre is similar to dp array that we computed in dynamic programming solutions and
    suf can be calculated in similar way, just by starting iteration from the end."""

# def maxSubArray(nums):
#     pre, suf = [*nums], [*nums]
#     for i in range(1, len(nums)):       pre[i] += max(0, pre[i-1])
#     for i in range(len(nums)-2,-1,-1):  suf[i] += max(0, suf[i+1])
#     def maxSubArray(A, L, R):
#         if L == R: return A[L]
#         mid = (L + R) // 2
#         return max(maxSubArray(A, L, mid), maxSubArray(A, mid+1, R), pre[mid] + suf[mid+1])
#     return maxSubArray(nums, 0, len(nums)-1)

# def maxSubArray(nums):
#     tempSum = 0
#     maxSum = nums[0]

#     for num in nums:
#         tempSum+=num

#         if tempSum>maxSum:
#             maxSum = tempSum

#         if tempSum<0:
#             tempSum = 0
#     return maxSum

if __name__ == "__main__":
    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
