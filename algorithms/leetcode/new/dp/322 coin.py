# def coinChange(coins, amount, memo=None):
#     if memo is None:
#         memo = {}
#     if amount == 0: return []
#     if amount in memo: return memo[amount]
#     if amount < 0: return None
#     shortest = None
#     for c in coins:
#         res = coinChange(coins, amount-c, memo)
#         if res is not None:
#             print(res, type(res))
#             combination = res + [c]
#             if shortest is None or len(combination) < len(shortest):
#                 shortest = combination
#     memo[amount] = shortest
#     return memo[amount]

class Solution(object):
    def coinChange(self, coins, amount, memo=None):
        def solve(coins, amount, memo=None):
            if memo is None:
                memo = {}
            if amount == 0: return []
            if amount in memo: return memo[amount]
            if amount < 0: return None
            shortest = None
            for c in coins:
                res = solve(coins, amount-c, memo)
                if res is not None:
                    combination = res + [c]
                    if shortest is None or len(combination) < len(shortest):
                        shortest = combination
            memo[amount] = shortest
            return memo[amount]
        return len(solve(coins, amount))

# def coinChange(coins, amount, memo=None):
#     if not coins:
#         return -1
#     dp = [float('inf')] * (amount + 1)
#     dp[0] = 0
#     for coin in coins:
#         for m in range(coin, amount + 1):
#             dp[m] = min(dp[m], dp[m - coin] + 1)

#     return dp[amount] if dp[amount] != float('inf') else -1

if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([2], 3))