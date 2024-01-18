# def findShortestSubArray(nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     degree = 0
#     counts = {}
#     for s in set(nums):
#         amount = nums.count(s)
#         degree = max(degree, amount)
#         counts[s] = amount
#     num_list = list(filter(lambda y: y[1] == degree, counts.items()))
#     count = len(nums)
#     while num_list:
#         to_fnd = num_list[0][0]
        
#         count = min(count, (len(nums)-nums[::-1].index(to_fnd))-nums.index(to_fnd))
#         num_list.pop(0)
#     return count

def findShortestSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    leftmost = {}
    rightmost = {}
    count = {}
    for idx, num in enumerate(nums):
        if num not in leftmost:
            leftmost[num] = idx
        rightmost[num] = idx
        count[num] = count.get(num, 0) + 1
    
    degree = max(count.values())
    min_len = len(nums)
    for num in count.keys():
        if count[num] == degree:
            min_len = min(min_len, rightmost[num] - leftmost[num] + 1)
    return min_len

if __name__ == "__main__":
    # findShortestSubArray([1,2,2,3,1,4,2])
    a = findShortestSubArray([1,2,2,3,1])
    print(a)