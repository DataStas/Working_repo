import sys
import random


# def MaxProduct(n, arr):
     
#     # if size is less than
#     # 4, no quadruple exists
#     if (n < 4):
#         return -1;
 
#     # will contain max product
#     max_product = -sys.maxsize;
 
#     for i in range(n - 3):
#         for j in range(i + 1, n - 2):
#             for k in range(j + 1, n - 1):
#                 for l in range(k + 1, n):
#                     max_product = max(max_product,
#                                       arr[i] * arr[j] *
#                                       arr[k] * arr[l])
 
#     return max_product

def MaxProduct(n, arr):
 
    # if size is less than 4, no
    # quadruple exists
    if (n < 4):
        return -1
 
    # Sort the array in ascending order
    arr.sort()
 
    x = (arr[n - 1] * arr[n - 2] *
         arr[n - 3] * arr[n - 4])
    y = arr[0] * arr[1] * arr[2] * arr[3]
    z = (arr[0] * arr[1] *
         arr[n - 1] * arr[n - 2])
 
    # Return the maximum of x, y and z
    return max(x, max(y, z))

# A O(n) Python 3 program to find maximum quadruple in# an array.
import sys
 
# Function to find a maximum product of a quadruple
# in array of integers of size n
def MaxProduct(n, arr):
    # if size is less than 4, no quadruple exists
    if (n < 4):
        return -1
 
    # Initialize Maximum, second maximum, third
    # maximum and fourth maximum element
    maxA = -sys.maxsize - 1
    maxB = -sys.maxsize - 1
    maxC = -sys.maxsize - 1
    maxD = -sys.maxsize - 1
 
    # Initialize Minimum, second minimum, third
    # minimum and fourth minimum element
    minA = sys.maxsize
    minB = sys.maxsize
    minC = sys.maxsize
    minD = sys.maxsize
 
    for i in range(n):
        # Update Maximum, second maximum, third
        # maximum and fourth maximum element
        if (arr[i] > maxA):
            maxD = maxC
            maxC = maxB
            maxB = maxA
            maxA = arr[i]
 
        # Update second maximum, third maximum
        # and fourth maximum element
        elif (arr[i] > maxB):
            maxD = maxC
            maxC = maxB
            maxB = arr[i]
 
        # Update third maximum and
        # fourth maximum element
        elif (arr[i] > maxC):
            maxD = maxC
            maxC = arr[i]
 
        # Update fourth maximum element
        elif (arr[i] > maxD):
            maxD = arr[i]
 
        # Update Minimum, second minimum
        # third minimum and fourth minimum element
        if (arr[i] < minA):
            minD = minC
            minC = minB
            minB = minA
            minA = arr[i]
 
        # Update second minimum, third
        # minimum and fourth minimum element
        elif (arr[i] < minB):
            minD = minC
            minC = minB
            minB = arr[i]
 
        # Update third minimum and
        # fourth minimum element
        elif (arr[i] < minC):
            minD = minC
            minC = arr[i]
 
        # Update fourth minimum element
        elif (arr[i] < minD):
            minD = arr[i]
 
    x = maxA * maxB * maxC * maxD
    y = minA * minB * minC * minD
    z = minA * minB * maxA * maxB
    # Return the maximum of x, y and z
    return max(x, max(y, z))

def test(min: int, max: int, size: int, test_num: int):
        a_test = [random.randint(min, max) for _ in range(size)]
        print(f'Test for {a_test}')
        correct_ans = MaxProduct(len(a_test), a_test)
        return correct_ans


if __name__ == '__main__':
    cur_test = 0
    tests = []
    test_num = 100
    n = [random.randint(4, 5) for _ in range(test_num)]
    while cur_test < test_num:
        print(f'Test {cur_test}')
        res = test(-10, 10, n[cur_test], cur_test)
        cur_test += 1
        print(res)
        print()