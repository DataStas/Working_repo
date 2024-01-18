# if __name__ == '__main__':    
#     n = int(input())
#     nums = list(map(int, input().split(' ')))
#     out = []
#     while nums:
#         cur = nums.pop()
#         count = 0
#         for ind, n in enumerate(nums[::-1]):
#             if cur > n:
#                 count += 1
#             else:
#                 break
#         out.append(count)
#     print(*out[::-1])


if __name__ == '__main__':    
    # n = int(input())
    # nums = list(map(int, input().split(' ')))
    s = '1 2 3 4 5'
    s1 = ''
    nums = list(map(int, s.split(' ')))
    out = []
    while nums:
        count = 0
        cur = nums.pop()
        it = -1
        next_n = nums[it] if nums else 10**5
        while cur > next_n and it > -(len(nums)+1):
            next_n = nums[it] 
            it -= 1
            count += 1
        out.append(count)
    print(out[::-1])
