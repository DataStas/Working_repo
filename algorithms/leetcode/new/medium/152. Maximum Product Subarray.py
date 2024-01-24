from cmath import inf

# Kadane ALgorithm
# def maxProduct(nums):
#     cur_max = 1
#     cur_min = 1
#     ans = -10**10

#     for x in nums:
#         tmp = cur_max
#         cur_max = max(x * cur_max, x * cur_min, x)
#         cur_min = min(x * cur_min, x * tmp, x)
#         ans = max(ans, cur_max)

#     return ans

def maxProduct(nums):
    maxi=-inf
    pref=1
    suff=1
    for i in range(0,len(nums)):
        if pref==0:
            pref=1
        if suff==0:
            suff=1
        pref*=nums[i]
        suff*=nums[len(nums)-1-i]
        maxi=max(maxi,pref,suff)
    return maxi

if __name__ == "__main__":
    print(maxProduct([-2,0,-1]))