# from typing import List
from datetime import datetime


def time_estimate(fun):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        res = fun(*args, **kwargs)
        tim = datetime.now() - start
        print(tim)
        return res
    return wrapper


def fib_memoization(fun):
    stack = {}

    def wrapper(n):
        if n in stack.keys():
            return stack[n]
        else:
            res = fun(n)
            stack[n] = res
            return res
    return wrapper

@time_estimate
@fib_memoization
def fib(n: int):
    if n <= 2:
        return 1
    return fib(n-1) + fib(n-2)

# def fib_memo(n: int, stack={}):
#     if n <= 2:
#         return 1
#     if n in stack:
#         return stack[n]
#     res = fib_memo(n-1, stack) + fib_memo(n-2, stack)
#     stack[n] = res
#     return res


def fib_memo(n: int, stack=None):
    if stack is None:
        stack = {}
    if n <= 2:
        return 1
    if n in stack:
        return stack[n]
    res = fib_memo(n-1, stack) + fib_memo(n-2, stack)
    stack[n] = res
    return res


if __name__ == "__main__":
    a = fib(35)
    print(a)
    res = fib_memo(300)
    print(res)