import random
from typing import List, Callable


# def lomuto_div(arr: List[int]):
#     out = [arr[0]]
#     lower = []
#     upper = []
#     for x in arr[1:]:
#         if x < arr[0]:
#             lower.append(x)
#         else:
#             upper.append(x)
#     out = [arr[0]] + lower + upper
#     out[0], out[len(lower)] = out[len(lower)], out[0]
#     return out

def lomuto_div(arr: List[int]):
    out = [-1] * len(arr)
    out[0] = arr[0]
    b, l = 1, 1
    for x in arr[1:]:
        if x < arr[0]:
            out[l], out[l+b-1] = x, out[l]
            l += 1
        else:
            out[b+l-1] = x
            b += 1
    out[0], out[l-1] = out[l-1], out[0]
    return out

def test(fun: Callable):
    # arr = [random.randint(1, 10) for _ in range(10)]
    arr = [4, 7, 2, 5, 3, 1, 8, 9, 6]
    print(fun(arr))


if __name__ == "__main__":
    test(lomuto_div)
# if __name__ == "__main__":
#     n = input()
#     arr = list(map(int, input().split()))
#     print(lomuto_div(arr))