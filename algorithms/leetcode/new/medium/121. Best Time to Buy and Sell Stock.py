def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    l = 0
    r = 1
    max_prof = 0
    while r < len(prices):
        profit = prices[r] - prices[l]
        if prices[l] > prices[r]:
            l = r
        else:
            max_prof = max(profit, max_prof)
        r += 1
    return max_prof

        # """
        # :type prices: List[int]
        # :rtype: int
        # """
        # if len(prices) < 2:
        #     return 0
        # max_prof = 0
        # min_p = 10**5
        # for p in prices:
        #     if p < min_p:
        #         min_p = p
        #     elif p - min_p > max_prof:
        #         max_prof = p - min_p

        # return max_prof
            
        
        

if __name__ == "__main__":
    print(maxProfit([7,1,5,3,6,4]))